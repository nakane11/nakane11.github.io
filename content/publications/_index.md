---
title: 論文
type: landing
cms_exclude: false

# Page sections
sections:
  - block: markdown
    content:
      title: 論文一覧
      text: |
        国際学会、査読論文誌などで発表した最近の研究成果をご紹介します。詳細な情報については、[ResearchMap プロフィール](https://researchmap.jp/a-nakane)もしくは[Google Scholar](https://scholar.google.com/)をご覧ください。

  - block: collection
    id: featured-papers
    content:
      title: 注目論文
      filters:
        folders:
          - publications
        featured_only: true
    design:
      view: article-grid
      columns: 2
      fill_image: false

  - block: collection
    id: journal-articles
    content:
      title: 査読論文誌
      text: 国際および国内の学術雑誌に掲載された査読論文
      filters:
        folders:
          - publications/journal-article
    design:
      view: citation
      columns: 1

  - block: collection
    id: conference-papers
    content:
      title: 国際学会論文
      text: 国際学会で発表した論文
      filters:
        folders:
          - publications/conference-paper
    design:
      view: citation
      columns: 1

  - block: collection
    id: domestic-conference
    content:
      title: 国内学会論文
      text: 国内学会で発表した論文
      filters:
        folders:
          - publications/domestic-conference
    design:
      view: citation
      columns: 1

  - block: collection
    id: preprints
    content:
      title: プレプリント・技術報告書
      text: プレプリントおよび技術報告書
      filters:
        folders:
          - publications/preprint
    design:
      view: citation
      columns: 1
---
