# listnr-server-sample-py

[日本語版](#listnr-server-sample-py-1)

This is a sample server for audio destination of Listnr.

* [Listnr product page](https://listnr.cerevo.com/en)
* Please refer to the [Online manual](https://listnr.cerevo.com/en/doc/) for how to setup Listnr.
* Please refer to [Information for developers](https://listnr.cerevo.com/en/developers/) for more information.
* This sample is for Python 2.7.

## Accept audio upload

* The sample program is in the “simple” directory.

### Installing dependencies

```
cd simple
pip install -r requirements.txt
```

### Running server

* Run server.

```
python server.py
```

* Open http://localhost:8080/ with a browser.

* Open another terminal and test audio upload.

```
cd audio_sample
curl -H "Transfer-Encoding: chunked" -X POST http://localhost:8080/wave -F "file=@sample.r16;type=application/octet-stream"
```

* Reload the page opened with a browser, then you will see the uploaded file.

![Simple page](/../assets/screenshot_simple.png?raw=true)


## Speech to text

### Installing dependencies

```
cd speech_to_text
pip install -r requirements.txt
```

### Create an account for a speech-to-text service

* This sample uses [IBM Bluemix Speech To Text](https://console.ng.bluemix.net/catalog/services/speech-to-text/) .
* Please create an account and get a username and password.
* Add your username and password in speech_to_text/config.ini.


### Running server

* Run server.

```
python server.py
```

* Open http://localhost:8080/ with a browser.

* Open another terminal and test audio upload.

```
cd audio_sample
curl -H "Transfer-Encoding: chunked" -X POST http://localhost:8080/wave -F "file=@sample.r16;type=application/octet-stream"
```

* Reload the page opened with browser, then you will see the uploaded file.

![Speech-to-text page](/../assets/screenshot_speech_to_text.png?raw=true)


### Initializing database

* Results are saved in textlog.sqlite3.
* To initialize the database, execute following command.

```
cd speech_to_text
sqlite3 textlog.sqlite3 < initdb.sql
```


## How to change the audio destination URL of Listnr.

* Select “Settings” in the navigation menu of the Listnr app.
* Select your Listnr in the “My Listnr” section to open “Listnr settings”.
* Select “Audio destination”.
* Select “Custom”.
* Input URL.
  * e.g. http://192.168.0.10:8080/wave
* Set “Recording time” if you want.
* Press the back button to return to “Listnr settings”.
* Make a sound to get Listnr to start audio uploading. Then Listnr will configure the new settings.
  * Listnr also configures new settings by powering off and on.


## How to create an audio file for testing

* Listnr uploads headerless linear PCM data.
  * Sample rate: 16kHz
  * Sample size: 16bit
  * Channels: 1

### Using SoX - Sound eXchange

* Install SoX from http://sox.sourceforge.net/ .
* To convert an mp3 file, execute the following command.

```
sox sample.mp3 -b 16 -c 1 -r 16000 -t raw sample.r16
```



# listnr-server-sample-py

Listnrの音声アップロードを受け付けるサーバーのサンプルプログラムです。

* [Listnr製品ページ](https://listnr.cerevo.com/ja)
* [オンラインマニュアル](https://listnr.cerevo.com/ja/doc/) を参考に、Listnrをセットアップした上でご利用ください。
* [開発者向け情報](https://listnr.cerevo.com/ja/developers/) も合わせてご参照ください。
* Python 2.7 で動作確認しています。

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
* 戻るボタンを押し、Listnr設定画面に戻ります。
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
