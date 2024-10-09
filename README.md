
# 必要な環境
- VSCode
    - 拡張機能　Django Python
- Git for Windows (Linuxなら普通にgitでもよい)
- Python（VSCodeのターミナル内でpythonと打てばwindowsストアが出てきてインストールできる）
- SQLiteBrowzer(https://sqlitebrowser.org/dl/)

## 実行までの設定
- `./install.sh`をGitBashのターミナルで実行
- コマンドパレット（Ctrl+Shift+P）で「Python:インタープリターを選択」で「'venv':venv」を選択
- ターミナルを新規起動
- `python manage.py createsuperuser`をGitBashのターミナルで実行し、下記の通りに入力
```
$ python manage.py createsuperuser
Username (leave blank to use 'hoge'): admin
Email address: admin@example.com
Password: password
Password (again): password
Superuser created successfully.
```
- デバッグ（▷に虫マークのアイコン）を表示して左上の▷マークをクリック
- ブラウザで→にアクセス　http://127.0.0.1:8000/polls/
- データを増やしたいときはブラウザで→にアクセス　http://127.0.0.1:8000/admin/
ログイン情報は上記

## modelsを追加したとき
- `python manage.py makemigrations XXXX`をGitBashのターミナルで実行（XXXXはフォルダ名　例：polls）

## アップデート時
- `./install.sh`をGitBashのターミナルで実行

## ライブラリ追加時
- `./freeze.sh`をGitBashのターミナルで実行
- そのままコミット




以上