import requests
import json

URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
APIKey = "AIzaSyC-hWXAslYYdHmE5IKjGAnn1QX7As8v3hE"

class Shops(object):
    def __init__(self, shops_data):
        self.shops_data = shops_data
        self.shops = self.set_shop(shops_data)
    
    def __getitem__(self, key):
        return self.shops[key]

    def __len__(self):
        return len(self.shops)

    def set_shop(self, shops_data):
        shops = []
        for i in range(len(shops_data)):
            shops.append(Shop(shops_data[i]))
        return shops


class Shop(object):
    def __init__(self, data):
        self.lat = data["geometry"]["location"]["lat"]
        self.lng = data["geometry"]["location"]["lng"]
        self.place_id = data["place_id"]
        self.name = data["name"]

        # 写真データのurl
        photo_maxwidth = 400
        google_photo_api = "https://maps.googleapis.com/maps/api/place/photo?key=" + APIKey
        photo_reference = data["photos"][0]["photo_reference"]
        
        self.photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth={photo_maxwidth}&photoreference={photo_reference}&key={APIKey}"

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

    # urlから情報を入手
    response = requests.get(get_url)
    if response.status_code == 200:
        print("success")   # HTTPのステータスコード取得
    else:
        print("requests failed")
    # json に整形
    respons_json = json.loads(response.text)
    return respons_json

if __name__ == "__main__":

    r = get_shops_data(43.059856, 141.343081, "convenience_store", 200)
    print("#######")
    print(r)
    shops = Shops(r["results"])
    print(len(shops)) # 店舗数の取得
    print(shops[0].name) # 一番目の店舗の名前
    print(shops[0].place_id) # 一番目の店舗のid
    print(shops[0].lng) # 一番目の店舗の緯度
    print(shops[0].lat) # 一番目の店舗の経度
    print(shops[2].photo_url)
    for i in range(len(shops)):
        print(shops[i].name) # n番目の店舗の名前
        print(shops[i].place_id) # n番目の店舗のid
        print(shops[i].lng) # n番目の店舗の緯度
        print(shops[i].lat) # n番目の店舗の経度
        print(shops[i].photo_url) # n番目の店舗の画像
        print(shops[i].google_map_url) #n番目の店舗のgoogle_map
    