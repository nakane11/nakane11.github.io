# Publications

BibTeX形式で論文情報を管理します。

## ファイル構成

- **international_conferences.bib** - 国際学会論文
- **domestic_conferences.bib** - 国内学会論文
- **journals.bib** - 査読論文誌
- **publications.bib** - 全論文の統合ファイル

## 論文の追加方法

### 1. 国際学会論文を追加する場合

`international_conferences.bib` に以下の形式で追加します：

```bibtex
@inproceedings{nakane2024example,
  title={論文タイトル},
  author={Nakane, Aoi},
  booktitle={学会名（ICRA, RO-MAN など）},
  pages={},
  year={2024},
  month={Month},
  address={開催地},
  organization={IEEE など},
  doi={10.xxxx/xxxx},
  url={https://doi.org/10.xxxx/xxxx},
  abstract={アブストラクト}
}
```

### 2. 国内学会論文を追加する場合

`domestic_conferences.bib` に以下の形式で追加します：

```bibtex
@inproceedings{nakane2024domestic,
  title={論文タイトル},
  author={Nakane, Aoi},
  booktitle={学会名},
  pages={},
  year={2024},
  month={月},
  organization={学会名},
  doi={10.xxxx/xxxx},
  url={https://doi.org/10.xxxx/xxxx},
  abstract={アブストラクト}
}
```

### 3. 論文誌に追加する場合

`journals.bib` に以下の形式で追加します：

```bibtex
@article{nakane2024journal,
  title={論文タイトル},
  author={Nakane, Aoi},
  journal={雑誌名},
  volume={巻号},
  number={号},
  pages={ページ数},
  year={2024},
  month={月},
  publisher={出版社},
  doi={10.xxxx/xxxx},
  url={https://doi.org/10.xxxx/xxxx},
  abstract={アブストラクト}
}
```

## 注意事項

- **publications.bib は自動生成** - 必要に応じてスクリプトで統合
- **cite key の形式** - `nakane年genre` で統一（例: `nakane2024warbe`）
- **著者名** - First name Last name の形式で統一
- **月の表記** - 英語表記（January, February など）
- **DOI と URL** - BibTeX内で以下のように指定：
  - `doi={10.xxxx/xxxx}` - DOI番号
  - `url={https://doi.org/10.xxxx/xxxx}` - DOIのハイパーリンク
  - BibTeXレンダラーがURLをハイパーリンク化します

## 既存の論文情報

- 2024: ICRA 2024（国際）
- 2023: RO-MAN 2023（国際）
- 2026: Journal of Robotics and Mechatronics（論文誌）
