SNEAKER TRACKER — 自動ニュース収集版

GitHub Pagesにファイルを配置し、GitHub Actionsを有効化すると約6時間おきにGoogle Newsの公開RSSからNIKE関連の発売・抽選ニュース見出しを収集します。

導入：ZIP内の sneaker_tracker フォルダの「中身」をリポジトリのルートにアップロード。隠しフォルダ .github/workflows/update-news.yml と scripts/update_news.py と data/news.json も必要です。GitHub Actions > Update sneaker news > Run workflow を一度実行。Settings > Actions > General > Workflow permissions で Read and write permissions が必要な場合があります。GitHub Pagesはmain/(root)を選択。

注意：ニュース見出しと元記事へのリンクを自動表示する機能です。発売日、抽選受付開始・締切、応募資格の確定情報ではありません。各販売元で必ず確認してください。公式NIKE/SNKRSの非公開APIは使用していません。Google News RSSの仕様変更やアクセス制限により更新できないことがあります。GitHub Actionsの実行間隔は保証されません。

手動登録したデータはブラウザのlocalStorageに保存されます。複数端末間の同期、プレ値自動取得、バックグラウンドの締切通知は未対応です。
