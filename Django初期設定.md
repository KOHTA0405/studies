# Getting Started

Djangoによるwebアプリケーション作成を行う際の初期設定

## 1. 適当なディレクトリの作成

　プロジェクトの作成にあたって、任意の場所に新しいディレクトリを作成

## 2. 作成したディレクトリの中にpythonの仮想環境を構築(venv)

- python3 -m venv [newenvname] (名前はvenvにするのが良い)
- source [newenvname]/bin/activate (仮想環境の有効化)

## 3. pipのアップグレード

　python3 -m pip install --upgrade pip

## 4. Djangoのインストール

　pip install django

　※python -m django --version (バージョン確認)

## 5. プロジェクトの作成

　django-admin startproject internal_sharing_project .

## 6. アプリの作成

　python manage.py startapp <アプリ名>

## 7. プロジェクトのsettings.pyファイルを編集

1. INSTALLED_APPSに'boardapp.apps.BoardappConfig'を追加(作成したアプリをプロジェクトに認識させる)
2. TEMPLATESにhtmlの保存場所となるディレクトリを記載('DIRS': [BASE_DIR / 'templates'])
3. urlのつなぎ込み
- プロジェクトのurls.pyにpath('', include('boardapp.urls'))を追加、includeをimport
- アプリ側にurls.pyを作成して、中身をコピーして、一旦adminのやつ以外は消す

