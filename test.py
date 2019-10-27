
from get_location import(get_shops_data,Shops)

r = get_shops_data(43.059856, 141.343081, "convenience_store", 200)
shops = Shops(r["results"])
print(len(shops)) # 店舗数の取得
print(shops[0].name) # 一番目の店舗の名前
print(shops[0].place_id) # 一番目の店舗のid
print(shops[0].lng) # 一番目の店舗の緯度
print(shops[0].lat) # 一番目の店舗の経度
print(shops[2].photo_url)