import json
from get_location import *

# 10コマで

def shop_json(shop, item=None):
    shop_json = json.loads(
    """
    {
        "type": "bubble",
        "header": {
          "type": "box",
          "layout": "vertical",
          "flex": 0,
          "contents": [
            {
              "type": "text",
              "text": "この店舗をお気に入り登録♡",
              "size": "lg",
              "align": "center",
              "weight": "bold",
              "color": "#EF93B6"
            },
            {
              "type": "separator"
            }
          ]
        },
        "hero": {
          "type": "image",
          "url": "https://crowdworks.jp/articles/wp-content/uploads/2018/12/1-62.jpg",
          "size": "full",
          "aspectRatio": "1.91:1",
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
              "text": "セブンイレブン{店舗名}",
              "size": "md",
              "weight": "bold"
            },
            {
              "type": "text",
              "text": "値引き商品数",
              "size": "md",
              "weight": "bold"
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
                      "text": "🥐パン...",
                      "flex": 1,
                      "size": "sm",
                      "color": "#000000"
                    },
                    {
                      "type": "text",
                      "text": "{商品個数}点",
                      "flex": 1,
                      "size": "sm",
                      "color": "#666666",
                      "wrap": true
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
                      "text": "🍙おにぎり...",
                      "flex": 1,
                      "size": "sm",
                      "color": "#000000"
                    },
                    {
                      "type": "text",
                      "text": "{商品個数}点",
                      "flex": 1,
                      "size": "sm",
                      "color": "#666666",
                      "wrap": true
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
                      "text": "🍱お弁当...",
                      "flex": 1,
                      "size": "sm",
                      "color": "#000000"
                    },
                    {
                      "type": "text",
                      "text": "{商品個数}点",
                      "flex": 1,
                      "size": "sm",
                      "color": "#666666",
                      "wrap": true
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
                      "text": "🍰デザート...",
                      "flex": 1,
                      "size": "sm",
                      "color": "#000000"
                    },
                    {
                      "type": "text",
                      "text": "{商品個数}点",
                      "flex": 1,
                      "size": "sm",
                      "color": "#666666",
                      "wrap": true
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
                "type": "postback",
                "label": "📌 行き方をを見る",
                "data": "01"
              },
              "style": "primary"
            }
          ]
        }
      }"""
    )
    shop_json["hero"]["url"] = shop.photo_url
    shop_json["body"]["contents"][0]["text"] = shop.name
    shop_json["footer"]["contents"][0]["action"]["data"] = shop.google_map_url
    return shop_json

def shops_json(shops):
    shops_json = json.loads(
    """
    {
    "type": "flex",
    "altText": "Flex Message",
    "contents": {
        "type": "carousel",
        "contents": [
        ]
    }
    }
    """)

    max_length = len(shops) if len(shops) < 10 else 10
    for i in range(max_length):
        shops_json["contents"]["contents"].append(shop_json(shops[i]))
    return shops_json


if __name__ == "__main__":
    r = get_shops_data(43.059856, 141.343081, "convenience_store", 200)
    print("#######")
    shops = Shops(r["results"])
    print(shops_json(shops))
    #print(shop_json(shops[0]))

# shops_json = json.loads(
# """
# {
#   "type": "flex",
#   "altText": "Flex Message",
#   "contents": {
#     "type": "carousel",
#     "contents": [
#     ]
#   }
# }
# """)