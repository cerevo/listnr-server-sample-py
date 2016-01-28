# listnr-server-sample-py

Listnrの音声アップロードを受け付けるサーバーのサンプルプログラムです。

* [Listnr製品ページ](https://listnr.cerevo.com/ja)
* [オンラインマニュアル](https://listnr.cerevo.com/ja/doc/) を参考に、Listnrをセットアップした上でご利用ください。
* [開発者向け情報](https://listnr.cerevo.com/ja/developers/) も合わせてご参照ください。
* Python 2.7.10 で動作確認しています。

## 音声アップロードを受け付ける

* simple ディレクトリ以下にサンプルプログラムがあります。

### セットアップ

```
cd simple
pip install -r requirements.txt
```

### 実行

* サーバーを起動する。

```
python server.py
```

* ブラウザで http://localhost:8080/ を開く。

* サーバーを起動したコンソールとは別のコンソールを開き、音声アップロードをテストする。

```
cd audio_sample
curl -H "Transfer-Encoding: chunked" -X POST http://localhost:8080/wave -F "file=@sample.r16;type=application/octet-stream"
```

* ブラウザで開いたページをリロードするとアップロードしたファイルが表示されるはずです。


## 音声認識する

### セットアップ

```
cd speech_to_text
pip install -r requirements.txt
```

### 音声認識サービスに登録する

* 本サンプルでは、[IBM Bluemix Speech To Text](https://console.ng.bluemix.net/catalog/services/speech-to-text/) を利用しています。
* 上記サービスに登録し、usernameとpasswordを取得してください。
* 取得した usernameとpassword を speech_to_text ディレクトリ以下の config.ini に保存してください。

### 実行

* サーバーを起動する。

```
python server.py
```

* ブラウザで http://localhost:8080/ を開く。

* サーバーを起動したコンソールとは別のコンソールを開き、音声アップロードをテストする。

```
cd audio_sample
curl -H "Transfer-Encoding: chunked" -X POST http://localhost:8080/wave -F "file=@sample.r16;type=application/octet-stream"
```

* ブラウザで開いたページをリロードするとアップロードしたファイルと認識されたテキストが表示されるはずです。


### データベースの初期化

* 認識されたテキストは、textlog.sqlite3 に保存されます。
* 初期化するには、以下のコマンドを実行します。

```
cd speech_to_text
sqlite3 textlog.sqlite3 < initdb.sql
```


## Listnrの音声アップロード先を変更する

* Listnrアプリのメニューから、各種設定を選択します。
* My Listnrセクションから、対象のListnrを選択し、Listnr設定画面を開きます。
* 設定セクションの音声アップロード先を選択します。
* 音声アップロード先設定画面で、カスタムを選択します。
* 音声アップロード先URLにURLを入力します。
  * 例: http://192.168.0.10:8080/wave
* 必要に応じて録音時間を設定します。
* 戻るボタンをおし、各種設定画面まで戻ります。
* Listnrに音を聞かせて、一度集音させます。これにより設定が反映されます。
  * 電源をオフ・オンすることでも設定が反映されます。

## テスト用音声データの作成方法

* Listnrはヘッダなしの非圧縮PCMデータを送信します。
  * サンプリング周波数: 16kHz
  * 量子化ビット数: 16bit
  * チャンネル数: 1
* 以下の手順で同様のデータを作成できます。

### SoX - Sound eXchange を使う

* http://sox.sourceforge.net/ をお使いの開発環境に合わせてインストールしてください。
* mp3ファイルを変換するには、以下のコマンドを実行します。

```
sox sample.mp3 -b 16 -c 1 -r 16000 -t raw sample.r16
```
