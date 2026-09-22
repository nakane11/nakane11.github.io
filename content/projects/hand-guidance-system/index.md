---
title: ロボットによる手繋ぎ誘導システム
featured: false
profile: false

# Optional external URL for project (instead of project page).
external_link: ""

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: ロボット手繋ぎ誘導システム
  focal_point: Smart

url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""

slides: ""
---

## 概要

手を繋ぐという自然な接触インタラクションを通じてロボットが人を案内するシステムの研究です。人がロボットの手を引いて先導しながら場所の名前を教えることで、ロボット自身が移動経路と場所を学習し、その後は自律的に人を案内できるようになります。さらに手繋ぎ可能な五指ロボットハンドを開発し、接触を伴う案内が利用者に与える心理的な安心感を実験的に検証しました。

## 手引きを用いた人の先導

- ロボットの手先に加わる仮想外力から、人が引く方向・強さを推定して移動速度を制御

## 人間からの場所教示による経路地図生成

- 先導中に通過した座標をノードとして記録し、経路をグラフ構造の地図として保存
- 人が「ここが〇〇だよ」と音声で話しかけると、その場の座標と場所の名前を対応づけて記憶
- 教示後は、目的地を伝えるだけでロボットが経路を探索し、自律移動で案内

## 手繋ぎ用五指ロボットハンド

人と手を繋ぐための五指ロボットハンドを搭載し、人へ手を差し出す動作から、案内中の手繋ぎ・解放、エレベータ利用時の中断までを一連の行動として実装しました。ハンド自体の設計・センシングについては独立したプロジェクト「[近接・力覚で握り状態を推定する五指ロボットハンド]({{< relref "/projects/grip-recognition-hand" >}})」で詳しく紹介しています。

## 心理的安心感の評価実験

- 手繋ぎありと手繋ぎなしの2条件で案内動画を100名の参加者に視聴してもらい、心理的安心感を7件法アンケートで比較
- 快適さ（Comfort）・性能感（Performance）で手繋ぎ条件がやや高い評価となる傾向を確認
- 手繋ぎによって案内ロボットに対する「有能さ」の印象が向上する一方、制御可能性（Controllability）の評価は低下する傾向も観測
- ロボットが手を差し出す動作は多くの参加者に「手繋ぎ」の意図として正しく伝わることを確認

## 関連論文

- 中根葵, 矢野倉伊織, 東風上奏絵, 岡田慧, 稲葉雅幸: 人の先導と場所教示をもとに案内行動を獲得するロボットの手繋ぎ誘導システム. *日本ロボット学会学術講演会*, 4D1-04, 2022.
- Aoi Nakane, Iori Yanokura, Aiko Ichikura, Kei Okada, Masayuki Inaba: Development of Robot Guidance System Using Hand-holding with Human and Measurement of Psychological Security. *IEEE International Symposium on Robot and Human Interactive Communication*, pp.2030-2036, 2023.
