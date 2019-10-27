from flask import Flask, request, abort, render_template,redirect
import urllib.request
from line_return_json import *

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)

import requests
import json
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
    SeparatorComponent, QuickReply, QuickReplyButton,ImageSendMessage
)
import datetime
import os
import time
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
        handler.handle(body,signature)
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
    elif event.message.text == "お気に入り店舗からバーゲン商品を検索": #ケース:お気に入り店舗からのバーゲン情報入手
        ###
        # お気にい入り店舗からのバーゲン情報入手 の処理
        ###
        return 
    if event.message.text == "hello":
        payload = payload = {
            "type": "flex",
            "altText": "Flex Message",
            "contents": {
                "type": "bubble",
                "hero": {
                "type": "image",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
                "size": "full",
                "aspectRatio": "20:13",
                "aspectMode": "cover",
                "action": {
                    "type": "uri",
                    "label": "Line",
                    "uri": "https://linecorp.com/"
                }
                },
                "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                    "type": "text",
                    "text": "Brown Cafe",
                    "size": "xl",
                    "weight": "bold"
                    },
                    {
                    "type": "box",
                    "layout": "baseline",
                    "margin": "md",
                    "contents": [
                        {
                        "type": "icon",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                        "size": "sm"
                        },
                        {
                        "type": "icon",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                        "size": "sm"
                        },
                        {
                        "type": "icon",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                        "size": "sm"
                        },
                        {
                        "type": "icon",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                        "size": "sm"
                        },
                        {
                        "type": "icon",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png",
                        "size": "sm"
                        },
                        {
                        "type": "text",
                        "text": "4.0",
                        "flex": 0,
                        "margin": "md",
                        "size": "sm",
                        "color": "#999999"
                        }
                    ]
                    },
                    {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "margin": "lg",
                    "contents": [
                        {
                        "type": "box",
                        "layout": "baseline",
                        "spacing": "sm",
                        "contents": [
                            {
                            "type": "text",
                            "text": "Place",
                            "flex": 1,
                            "size": "sm",
                            "color": "#AAAAAA"
                            },
                            {
                            "type": "text",
                            "text": "Miraina Tower, 4-1-6 Shinjuku, Tokyo",
                            "flex": 5,
                            "size": "sm",
                            "color": "#666666",
                            "wrap": True
                            }
                        ]
                        },
                        {
                        "type": "box",
                        "layout": "baseline",
                        "spacing": "sm",
                        "contents": [
                            {
                            "type": "text",
                            "text": "Time",
                            "flex": 1,
                            "size": "sm",
                            "color": "#AAAAAA"
                            },
                            {
                            "type": "text",
                            "text": "10:00 - 23:00",
                            "flex": 5,
                            "size": "sm",
                            "color": "#666666",
                            "wrap": True
                            }
                        ]
                        }
                    ]
                    }
                ]
                },
                "footer": {
                "type": "box",
                "layout": "vertical",
                "flex": 0,
                "spacing": "sm",
                "contents": [
                    {
                    "type": "button",
                    "action": {
                        "type": "uri",
                        "label": "CALL",
                        "uri": "https://linecorp.com"
                    },
                    "height": "sm",
                    "style": "link"
                    },
                    {
                    "type": "button",
                    "action": {
                        "type": "uri",
                        "label": "WEBSITE",
                        "uri": "https://linecorp.com"
                    },
                    "height": "sm",
                    "style": "link"
                    },
                    {
                    "type": "spacer",
                    "size": "sm"
                    }
                ]
                }
            }
        }
        container_obj = FlexSendMessage.new_from_json_dict(payload)
        line_bot_api.reply_message(event.reply_token, messages=container_obj)

@handler.add(MessageEvent, message=LocationMessage)
def handle_location(event):
    latitude = event.message.latitude
    longitude = event.message.longitude
    results = get_shops_data(latitude, longitude, "convenience_store", 200)
    shops = Shops(results["results"])
    
    shopIDs = []
    for shop in shops:
        shopIDs.append(shop.place_id)
    print(f"shopIDs:{shopIDs}")
    
    has_shops = dict()  #廃棄を持っているお店を格納する
    i=0
    for shopID in shopIDs:
        sql = f"SELECT storeid,COUNT(CASE WHEN jancode LIKE '1%' THEN 1 END), COUNT(CASE WHEN jancode LIKE '2%' THEN 2 END), COUNT (CASE WHEN jancode LIKE '3%' THEN 3 END) FROM stores WHERE storeid = '{shopID}' AND expirationdata < current_timestamp GROUP BY storeid;" ##ここではバーゲン条件を
        with conn.cursor() as cur:
            cur.execute(sql) #executeメソッドでクエリを実行。
            r=cur.fetchall()
            print(r)
            if [] != r:
                has_shops[r[0][0]] = [r[0][1],r[0][2],r[0][3]]
        i += 1

    print(f"has_shops_len:{len(has_shops)}\nshops:{has_shops}")
    if len(has_shops) == 0:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text = "現在、お探ししたところバーゲン商品がお近くにございません。\n時間を置いてもう一度お試しください。")
        )

    elif len(has_shops): # 1以上
        payload = json.loads(shops_json(shops, has_shops))
        print(payload)
        container_obj = FlexSendMessage.new_from_json_dict(payload)
        line_bot_api.reply_message(event.reply_token, messages=container_obj)
    
    #####################################################################################################

@app.route("/notice",methods = ['POST'])
def notice(event):
    #ユーザに店舗フレックスを送る。
    return 

@handler.add(PostbackEvent)#店舗フレックスでユーザから返信がきたとき。
def handle_postback(event):
    #帰ってきた label によって「お気に入り登録処理」と「商品フレックス返信処理」かを識別
    if event.postback.data == "favorite_store":
        storeID = event.postback.data # ポストバックの中から、storeidをサルベージ
        userID = event.source.userId
        ###
        # DBにアクセスを行い,table:usersにお気に入り店舗とユーザIDをインサートする。
        ###
        return
    if event.postback.data == "serch_product":
        return
    if event.postback.data == "0" or event.postback.data =="1": #アンケート1
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(
                text = "続いて、年齢について教えてください。",
                quick_reply = QuickReply(
                    items = [
                        QuickReplyButton(
                            action = PostbackAction(label = "~20歳",data = "2")
                        ),
                        QuickReplyButton(
                            action = PostbackAction(label = "21~40歳",data = "2")
                        ),
                        QuickReplyButton(
                            action = PostbackAction(label = "41~60歳",data = "2")
                        ),
                        QuickReplyButton(
                            action = PostbackAction(label = "61~歳",data = "2")
                        )
                    ]
                )
            )
        )
    if event.postback.data =="2" :
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(
                text = "続いて、コンビニにはどれぐらいの頻度で行きますか？",
                quick_reply = QuickReply(
                    items = [
                        QuickReplyButton(
                            action = PostbackAction(label = "1日1回",data = "3")
                        ),
                        QuickReplyButton(
                            action = PostbackAction(label = "3日1回",data = "3")
                        ),
                        QuickReplyButton(
                            action = PostbackAction(label = "1週間に1回",data = "3")
                        ),
                        QuickReplyButton(
                            action = PostbackAction(label = "2週間に1回",data = "3")
                        )
                    ]
                )
            )
        )
    if event.postback.data=="3":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="アンケートありがとうございます!\nあなたに最適な情報を今後お伝えします！")
        )
@handler.add(FollowEvent)
def handle_follow(event):
    #取得したユーザーIDをDBに格納する
    userID = event.source.user_id
    #display_nameを取得する。
    profile = line_bot_api.get_profile(userID)
    name = profile.display_name

    sql = f"INSERT INTO users(userid,storeid) VALUES ('{userID}','tekitou');"
    with conn.cursor() as cur:
        cur.execute(sql)

    line_bot_api.push_message(
        userID,
        TextSendMessage(
            text = " お友達登録ありがとうございます。\n日本の食品ロス問題を解決するためにお近くのコンビニの割引情報をご紹介するSaveFoodsです。",
        )
    )
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(
            text = f"4問の質問で{name}さんに最適な割引情報を ご紹介させていただきます。 まずは、{name}さん性別について教えてください。",
            quick_reply = QuickReply(
                items = [
                    QuickReplyButton(imageUrl = 'https://i.imgur.com/CGLeZ4q.png',action = PostbackAction(label = "男性",data = "1")),
                    QuickReplyButton(imageUrl = 'https://i.imgur.com/MLBUHSP.png',action = PostbackAction(label = "女性",data = "0"))
                ]
            )
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

URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
APIKey = "AIzaSyDI16v0Y33dykza423BcS_lgG6cr78a9iY"

class Shops(object):
    def __init__(self, shops_data):
        print("1")
        self.shops_data = shops_data
        print("2")
        self.shops = self.set_shop(shops_data)
    
    def __getitem__(self, key):
        return self.shops[key]

    def __len__(self):
        return len(self.shops)

    def set_shop(self, shops_data):
        shops = []
        print("3")
        for i in range(len(shops_data)):
            print(i)
            shops.append(Shop(shops_data[i]))
        return shops


class Shop(object):
    def __init__(self, data):
        print("100")
        self.lat = data["geometry"]["location"]["lat"]
        self.lng = data["geometry"]["location"]["lng"]
        self.place_id = data["place_id"]
        self.name = data["name"]

        # 写真データのurl
        photo_maxwidth = 400
        google_photo_api = "https://maps.googleapis.com/maps/api/place/photo?key=" + APIKey
        try:
            photo_reference = data["photos"][0]["photo_reference"]
            self.photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth={photo_maxwidth}&photoreference={photo_reference}&key={APIKey}"
        except:
            self.photo_url = "  "

        self.google_map_url = f"https://www.google.com/maps/search/?api=1&query=Google&query_place_id={self.place_id}"

        

def get_shops_data(lng, lat, types, radius, language="ja"):
    """
    params:
        lng: float 緯度
        lat: float 軽度
        type: 場所の種類
            {
                convenience_store : コンビニ
            }
        radius: その場所からの半径[m]
        language: 返り値の言語

    return: r
        {
            "html_attributions": [],
            "results": [
                {
                    "geometry": {
                        "location": {
                            "lat": 43.0597671, // 緯度
                            "lng": 141.3427528 // 軽度
                        },
                        "viewport": {
                            "northeast": {
                                "lat": 43.0610470802915,
                                "lng": 141.3441145302915
                            },
                            "southwest": {
                                "lat": 43.0583491197085,
                                "lng": 141.3414165697085
                            }
                        }
                    },
                    "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/shopping-71.png",
                    "id": "011df5345fe4930bacfd5ed0390a558c38c00cfa",
                    "name": "セブン-イレブン 札幌大通西９丁目店",
                    "opening_hours": {
                        "open_now": true
                    },
                    "photos": [
                        {
                            "height": 854,
                            "html_attributions": [
                                "<a href=\"https://maps.google.com/maps/contrib/108633365460714341799/photos\">川崎康</a>"
                            ],
                            "photo_reference": "CmRaAAAAMsfGFRSU1cjHThG2vwmjm_KopOFb0LsLwUoajOf0PaPkUqVomyTJWpeiS_v690nYm3eq1QqFvudWHXQSN8tbmVgPwvRygnyLhoXgCuxdi2HLE691RgeSYmwECwkjPbdDEhCfinA3XgG5o1y-QKqTkgi7GhTCAylEf3eDs7Mop6rOm4oZ8iwVPQ",
                            "width": 1519
                        }
                    ],
                    "place_id": "ChIJawtLJJopC18RHsPOv1BZGVs",
                    "plus_code": {
                        "compound_code": "385V+W4 日本、北海道 札幌市",
                        "global_code": "8RM3385V+W4"
                    },
                    "rating": 3.4,
                    "reference": "ChIJawtLJJopC18RHsPOv1BZGVs",
                    "scope": "GOOGLE",
                    "types": [
                        "convenience_store",
                        "food",
                        "point_of_interest",
                        "store",
                        "establishment"
                    ],
                    "user_ratings_total": 5,
                    "vicinity": "札幌市中央区大通西９丁目３−３３"
                },
                ]
            }
    """
    # urlを生成
    params = {}
    params["location"] = f"{lng},{lat}"
    params["types"] = types
    params["radius"] = radius
    params["language"] = language
    get_url = URL + "?key=" + APIKey
    for key, value in params.items():
        value = str(value) if type(value) != "string" else value
        get_url += "&" + key + "=" + value
    print(f"url is {get_url}")

    # urlから情報を入手
    response = requests.get(get_url)
    if response.status_code == 200:
        print("success")
    else:
        print("requests failed")  

    print(response.text)
    # HTTPのステータスコード取得
    # json に整形
    respons_json = json.loads(response.text)
    print(respons_json)
    return respons_json

if __name__ == "__main__":
    app.run()