# PJ13: Auto-Social-Listening

## 背景と目的
SNS から関連投稿を集め、Gemini でセンチメント分析とキーフレーズ抽出を行い、結果を可視化する Web アプリです。キーワードを入力するだけで 15 分以内にレポートを生成します。

## システム構成
![arch](pj13_architecture.png)

## セットアップ
```bash
cp .env.example .env  # GEMINI_API_KEY を設定
docker compose up --build
```

## 使い方
1. フロントエンドにアクセスしキーワードを入力
2. しばらく待つと結果画面に棒グラフ・円グラフとサマリが表示されます

## 環境変数
- `GEMINI_API_KEY` : Gemini API キー
- `VITE_API_BASE` : フロントエンド用 API ベース URL

## ライセンス
MIT
