from flask import Flask, request, abort, render_template,redirect


from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CameraAction, CameraRollAction, LocationAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent,
    SeparatorComponent, QuickReply, QuickReplyButton,
)
import datetime
import os
import psycopg2
from module import get_location

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
    elif event.message.text == "現在地から検索": #ケース:現在地からのバーゲン情報入手
        ###
        # 現在地からのバーゲン情報入手の処理
        ###
        #1.リッチメニュ-からのリクエスト到着

        #2.
        return 
    elif event.message.text == "お気に入り店舗からバーゲン商品を検索": #ケース:お気に入り店舗からのバーゲン情報入手
        ###
        # お気にい入り店舗からのバーゲン情報入手 の処理
        ###
        return 
@handler.add(MessageEvent, message=LocationMessage)
def handle_location(event):
    latitude = event.message.latitude
    longitude = event.message.longitude
    results = get_location.get_shop_data(lng=longitude,lat=latitude,types="convenience_store",radius=200)
    shops = get_location.Shop(results["results"])
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(
            text = shops[0].name
        )
    )   



@app.route("/notice",methods = ['POST'])
def notice(event):
    #ユーザに店舗フレックスを送る。
    return 

@handler.add(PostbackEvent)#店舗フレックスでユーザから返信がきたとき。
def handle_postback(event):
    #帰ってきた label によって「お気に入り登録処理」と「商品フレックス返信処理」かを識別
    if event.postback.label == "favorite_store":
        storeID = event.postback.data # ポストバックの中から、storeidをサルベージ
        userID = event.source.userId
        ###
        # DBにアクセスを行い,table:usersにお気に入り店舗とユーザIDをインサートする。
        ###
        return
    if event.postback.label == "serch_product":
        return
@handler.add(FollowEvent)
def handle_follow(event):
    #取得したユーザーIDをDBに格納する
    userID = event.source.user_id
    #display_nameを取得する。
    profile = line_bot_api.get_profile(userID)
    name = profile.display_name

    sql = f"INSERT INTO users(userid) VALUES ('{userID}');"
    with conn.cursor() as cur:
        cur.execute(sql)

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(
            text = "友達追加。ありがとな。"
        )
    )
#ブロックイベント
@handler.add(UnfollowEvent)
def handle_unfollow(event):
    userID = event.source.user_id
    #UserIDをデータベースから削除する
    sql = f"DELETE FROM users WHERE userid = '{userID}';"
    with conn.cursor() as cur:
        cur.execute(sql)


