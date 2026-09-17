#!/usr/bin/env python3
"""
Convert BibTeX files to Markdown format for display on Hugo site.
This script reads BibTeX files from the publications directory and updates _index.md.
"""

import re
from pathlib import Path
from collections import defaultdict

def parse_bibtex(content):
    """Parse BibTeX content and extract entries."""
    entries = []
    # Match @type{key, ... } patterns
    pattern = r'@(\w+)\{([^,]+),\s*(.*?)\n\}'

    for match in re.finditer(pattern, content, re.DOTALL):
        entry_type = match.group(1)
        entry_key = match.group(2).strip()
        fields_text = match.group(3)

        # Parse fields
        fields = {}
        field_pattern = r'(\w+)\s*=\s*\{([^}]*)\}'
        for field_match in re.finditer(field_pattern, fields_text):
            field_name = field_match.group(1).lower()
            field_value = field_match.group(2).strip()
            fields[field_name] = field_value

        entries.append({
            'type': entry_type.lower(),
            'key': entry_key,
            'fields': fields
        })

    return entries

def format_authors(author_string):
    """Format author string as: A. LastName, B. LastName, etc.
    Handles both "FirstName LastName" and "LastName, FirstName" formats."""
    if not author_string:
        return ""
    # Split by ' and '
    authors = [a.strip() for a in author_string.split(' and ')]
    formatted = []
    for author in authors:
        if ',' in author:
            # Format: "LastName, FirstName"
            parts = author.split(',')
            last_name = parts[0].strip()
            first_name = parts[1].strip() if len(parts) > 1 else ""
            if first_name:
                first_initial = first_name.split()[0][0]
                formatted.append(f"{first_initial}. {last_name}")
            else:
                formatted.append(last_name)
        else:
            # Format: "FirstName LastName"
            parts = author.split()
            if len(parts) >= 2:
                first_initial = parts[0][0]
                last_name = parts[-1]
                formatted.append(f"{first_initial}. {last_name}")
            else:
                formatted.append(author)
    return ', '.join(formatted)

def generate_markdown():
    """Generate markdown content from BibTeX files."""
    pub_dir = Path(__file__).parent.parent / 'publications'

    # Read from different categories
    files_to_read = [
        ('journals.bib', '## 査読論文誌'),
        ('international_conferences.bib', '## 国際学会'),
        ('domestic_conferences.bib', '## 国内学会'),
    ]

    all_entries = []

    for filename, section_title in files_to_read:
        filepath = pub_dir / filename
        if filepath.exists():
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            entries = parse_bibtex(content)

            # Sort by year (descending)
            entries.sort(key=lambda e: e['fields'].get('year', '0000'), reverse=True)

            # Add section title and entries
            all_entries.extend([(section_title, e) for e in entries])

    # Generate markdown with numbering across all sections
    output_lines = []
    current_section = None
    number = 1

    for section_title, entry in all_entries:
        if section_title != current_section:
            if current_section is not None:
                output_lines.append('')
            output_lines.append(section_title)
            output_lines.append('')
            current_section = section_title

        fields = entry['fields']
        title = fields.get('title', 'Unknown Title')
        authors = format_authors(fields.get('author', ''))
        year = fields.get('year', '')
        venue = fields.get('booktitle', fields.get('journal', ''))
        pages = fields.get('pages', '')
        volume = fields.get('volume', '')
        number_field = fields.get('number', '')

        # Format based on type
        if entry['type'] == 'article':
            # Journal article
            citation = f"{number}. {authors} ({year}). \"{title}.\" *{venue}"
            if volume:
                citation += f" {volume}"
            if number_field:
                citation += f"({number_field})"
            if pages and pages.strip():
                citation += f": {pages}"
            citation += "*."
        else:
            # Conference proceedings
            citation = f"{number}. {authors} ({year}). \"{title}.\" *{venue}"
            if pages and pages.strip():
                citation += f", pp. {pages}"
            citation += "*."

        output_lines.append(citation)
        number += 1

    output_lines.append('')
    output_lines.append('詳細は [ResearchMap](https://researchmap.jp/a-nakane) をご参照ください。')

    return '\n'.join(output_lines)

def update_index_md():
    """Update the _index.md file with the generated markdown content."""
    project_root = Path(__file__).parent.parent
    index_file = project_root / 'content' / 'publications' / '_index.md'

    # Generate new markdown content
    markdown_text = generate_markdown()

    # Read the current file
    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace the text section
    # Find the text: |
    lines = content.split('\n')
    new_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        new_lines.append(line)

        if 'text: |' in line:
            # Found the text section, replace until we find the next section
            i += 1
            # Skip the old content until we find a line that starts with less indentation
            base_indent = len(lines[i]) - len(lines[i].lstrip())
            while i < len(lines):
                if lines[i].strip() and not lines[i].startswith(' ' * (base_indent + 2)):
                    # We've reached the next section
                    break
                i += 1

            # Add the new markdown content with proper indentation
            indent = '        '
            for md_line in markdown_text.split('\n'):
                new_lines.append(indent + md_line)

            # Continue from where we left off
            continue

        i += 1

    # Write the updated file
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_lines))

    print(f"Updated {index_file}")

if __name__ == '__main__':
    update_index_md()
