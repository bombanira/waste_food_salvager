from flask import Flask, request, abort, render_template,redirect


from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)

import os
import psycopg2

####
# DBとのコネクション
conn = psycopg2.connect(
    '''
    dbname=d4bli17istimjb 
    host=ec2-174-129-43-40.compute-1.amazonaws.com
    user=jbzvogvoorcldg
    password=a87ca8b49a7286eff37cd854e52196e0e4e996feca64e19701dad2a8df3b704d
    '''
)
conn.autocommit = True


#アクセスキーの取得
app = Flask(__name__)
#Botの認証
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

@app.route("/callback",methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text = True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #https://developers.line.biz/console/channel/1653365219/basic/
    #LINEコンソールのwebhook URL のエラー回避用.
    if event.reply_token == "00000000000000000000000000000000": 
        return 

    if event.message.text == "お気に入り店舗の登録": #ケース：お気に入り店舗の検索
        ###
        # お気に入りの店舗の検索&登録
        ###
        return 
    elif event.message.text == "現在地からのバーゲン情報の入手": #ケース:現在地からのバーゲン情報入手
        ###
        # 現在地からのバーゲン情報入手の処理
        ###
        return 
        #1.リッチメニュ-からのリクエスト到着

        #2.
        return 
    elif event.message.text == "お気に入り店舗からバーゲン商品を検索": #ケース:お気に入り店舗からのバーゲン情報入手
        ###
        # お気にい入り店舗からのバーゲン情報入手 の処理
        ###
        return 

@app.route("/notice",methods = ['POST'])
def notice():
    #ユーザに店舗フレックスを送る。
    return 
