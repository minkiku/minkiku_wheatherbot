#coding:utf-8

import requests
import datetime

# お天気情報
url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
keydata = {"city": "140010"}
data = requests.get(url, params=keydata).json()

"""
0: 今日
1: 明日
2: 明後日
"""
i = 0

# アカウント名に表示する天気マークを作成
today = (data['forecasts'][i]['telop'])

"""
晴れ：9728
曇り：9729
雨：127783
雪：9731
"""
if today == '晴れ':
    weather = chr(9728)
elif today == '曇り':
    weather = chr(9729)
elif today == '雨':
    weather = chr(127783)
elif today == '晴のち曇':
    weather = chr(9728) + 'のち' + chr(9729)
elif today == '晴時々曇':
    weather = chr(9728) + 'ときどき' + chr(9729)
elif today == '晴れのち雨':
    weather = chr(9728) + 'のち' + chr(127783)
elif today == '晴時々雨':
    weather = chr(9728) + 'ときどき' + chr(127783)
elif today == '曇のち晴':
    weather = chr(9729) + 'のち' + chr(9728)
elif today == '曇時々晴':
    weather = chr(9729) + 'ときどき' + chr(9728)
elif today == '曇のち雨':
    weather = chr(9729) + 'のち' + chr(127783)
elif today == '曇時々雨':
    weather = chr(9729) + 'ときどき' + chr(127783)
elif today == '雨のち晴':
    weather = chr(127783) + 'のち' + chr(9728)
elif today == '雨時々晴':
    weather = chr(127783) + 'ときどき' + chr(9728)
elif today == '雨のち曇':
    weather = chr(127783) + 'のち' + chr(9729)
elif today == '雨時々曇':
    weather = chr(127783) + 'ときどき' + chr(9729)
elif today == '晴のち雨':
    weather = chr(9728) + 'のち' + chr(127783)
else:
    weather = today

# Bioに表示する最高気温と最低気温を出力
# APIから気温が NULL でかえってきたときは -- を出力
temMax = (data['forecasts'][i]['temperature']['max'])
if temMax is None:
    temMax = '--'
else:
    temMax = (data['forecasts'][i]['temperature']['max']['celsius'])
temMin = (data['forecasts'][i]['temperature']['min'])
if temMin is None:
    temMin = '--'
else:
    temMin = (data['forecasts'][i]['temperature']['min']['celsius'])

# tweet本文に表示する場所やリンクを取得
Location = (data['pinpointLocations'][0])
city = (Location['name'])
Link = (Location['link'])

# 本文に表示する時刻の取得
Now = datetime.datetime.now() + datetime.timedelta(hours=9)
DatetimeNow = Now.strftime('%Y/%m/%d %H:%M:%S')

