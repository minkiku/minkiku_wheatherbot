# coding:utf-8

import sys
sys.path.append('/path/to/dir')
import tweepy
from secret import *
from weatherAPI import *

# 認証
auth = tweepy.OAuthHandler(C_Key, C_S_Key)
auth.set_access_token(Tkn, Tkn_S)
api = tweepy.API(auth)

# アカウント名を作成
api.update_profile(name='みんきく' + '[ ' + weather + ' ]')

# Tweet本文を作成
api.update_status('【Weather Forecast from TweetBot】\n'
+ '今日の'+ city +'の天気は【' + today + '】です。\n'
+ '( 最高気温: ' + temMax + '℃ / 最低気温: ' + temMin + '℃ )\n'
+ '\n[ 更新: ' + DatetimeNow + ' ]\n' + Link)

# Bio を作成
api.update_profile(description='24歳 // 👩‍💻 / ' + chr(127927) +' / 東京家政 短大栄養科 / 須賀学59期' + '【 最高気温: ' + temMax + '℃ / 最低気温: ' + temMin + '℃ 】')