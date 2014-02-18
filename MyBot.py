#coding:utf-8
"""
Copyright (c) 2014. Kensuke Kousaka

This software is released under the MIT License

http://opensource.org/licenses/mit-license.php
"""
__author__ = 'kousaka'

import twitter, t_key, datetime, math, pywapi

# 認証鍵の取得
api_key = t_key.consumer_key
api_secret = t_key.consumer_secret
access_token_key = t_key.access_token
access_token_secret = t_key.access_token_secret

# 認証鍵を使ってOAuth認証を行い，APIを取得する
api = twitter.Api(api_key, api_secret, access_token_key, access_token_secret)

# 現在時刻を取得する
hour = datetime.datetime.today().hour
minute = datetime.datetime.today().minute

# minuteが1桁の場合
if 1 == int(math.log10(minute) + 1):
	#hourとminuteをstringに変換
	hour_string = str(hour)
	minute_string = '0' + str(minute)

	time_string = hour_string + minute_string

	#stringをintに変換
	time = int(time_string)
else:
	#hourとminuteをstringに変換
	hour_string = str(hour)
	minute_string = str(minute)

	time_string = hour_string + minute_string

	#stringをintに変換
	time = int(time_string)

# 天気情報を取得（神戸）
weather_com_result = pywapi.get_weather_from_weather_com('JAXX0040')

if 2150 < time < 2210:
	tweet_text = "@" + "kensuke_linx" + " " + u"22時です．もうそろそろ寝よう."

	# Tweetする
	api.PostUpdate(status=tweet_text)
elif 550 < time < 610:
	tweet_text = "@" + "kensuke_linx" + " " + u"6時です．もうそろそろ起きよう．"

	# Tweetする
	api.PostUpdate(status=tweet_text)

	# 天気情報をTweetする
	tweet_text = "@" + "kensuke_linx" + " " + u"今日の神戸の天気は" \
				 + weather_com_result['current_conditions']['text'] + u"，気温は" \
				 + weather_com_result['current_conditions']['temperature'] + u"℃です．"

	api.PostUpdate(status=tweet_text)
else:
	tweet_text = "@" + "kensuke_linx" + " " + "Error"
	api.PostUpdate(status=tweet_text)
