---
title: 'プロジェクト'
date: 2024-05-19
type: landing

# Page sections
sections:
  - block: markdown
    content:
      title: 研究プロジェクト
      text: |
        ロボティクス、触覚センシング、人間-ロボット相互作用に焦点を当てた最近の研究プロジェクトをご紹介します。各プロジェクトは、実践的なシステム開発と厳密な評価を組み合わせています。

  - block: collection
    content:
      title: 主要プロジェクト
      text: ''
      filters:
        folders:
          - projects
        featured_only: true
    design:
      view: article-grid
      fill_image: true
      columns: 2

  - block: collection
    content:
      title: すべてのプロジェクト
      filters:
        folders:
          - projects
    design:
      view: article-grid
      fill_image: false
      columns: 2
      show_date: true
---
