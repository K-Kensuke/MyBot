#coding:utf-8
"""
Copyright (c) 2014. Kensuke Kousaka

This software is released under the MIT License

http://opensource.org/licenses/mit-license.php
"""
__author__ = 'kousaka'

import datetime
import pywapi
import re

import twitter

import t_key

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
if minute < 10:
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

# 5:50~6:10
if 550 < time < 610:
	tweet_text = "@" + "kensuke_linx" + " " + u"22時です．もうそろそろ寝よう."

	# Tweetする
	api.PostUpdate(status=tweet_text)

# 12:50~13:10
elif 1250 < time < 1310:
	# HomeTimelineを取得する（リプライを除去した直近の100個）
	timeline = api.GetHomeTimeline(count=100, exclude_replies=True)

	# IFTTTが自動TweetしたUP by JawboneのSleep Feedを入れるリスト
	matchList = []

	# Sleep Feedのみを抽出する
	for match in timeline:
		regex = re.match('I fell asleep', match.text)

		if regex is not None:
			matchList.append(match.text)

	# 最新のSleep Feedを入れる
	sleepLog = matchList[0]

	# パーセント表示が小数点以下1桁の場合と2桁の場合で条件分けする
	regex = re.match('\(', sleepLog[sleepLog.index('%') - 5])

	if regex is not None:
		# 小数点以下1桁の場合
		percentageOfDeepSleep = sleepLog[sleepLog.index('%') - 4:sleepLog.index('%') - 2]

	else:
		percentageOfDeepSleep = sleepLog[sleepLog.index('%') - 5:sleepLog.index('%') - 3]

	# Stringをintにする
	deepSleep = int(percentageOfDeepSleep)

	if deepSleep < 60:
		tweet_text = "@" + "kensuke_linx" + " " + u"睡眠が足りていません．昼寝をおすすめします．"

		api.PostUpdate(status=tweet_text)

# 21:50~22:10
elif 2150 < time < 2210:
	tweet_text = "@" + "kensuke_linx" + " " + u"6時です．もうそろそろ起きよう．"

	# Tweetする
	api.PostUpdate(status=tweet_text)

	# 天気情報を取得（神戸と高槻）
	result_Kobe = pywapi.get_weather_from_weather_com('JAXX0040')
	result_Takatsuki = pywapi.get_weather_from_weather_com('JAXX0083')

	# 神戸の天気情報をTweetする
	weather_Kobe = "@" + "kensuke_linx" + " " + u"今日の神戸は" \
					+ result_Kobe['forecasts'][0]['day']['text'] + u"，気温は" \
					+ result_Kobe['forecasts'][0]['low'] + u"~" + result_Kobe['forecasts'][0]['high'] \
					+ u"℃，湿度は" + result_Kobe['forecasts'][0]['day']['humidity'] + u"%，降水確率は" \
					+ result_Kobe['forecasts'][0]['day']['chance_precip'] + u"%です．"

	api.PostUpdate(status=weather_Kobe)

	# 高槻の天気情報をTweetする
	weather_Takatsuki = "@" + "kensuke_linx" + " " + u"今日の高槻は" \
						+ result_Takatsuki['forecasts'][0]['day']['text'] + u"，気温は" \
						+ result_Takatsuki['forecasts'][0]['low'] + u"~" + result_Takatsuki['forecasts'][0]['high'] \
						+ u"℃，湿度は" + result_Takatsuki['forecasts'][0]['day']['humidity'] + u"%，降水確率は" \
						+ result_Takatsuki['forecasts'][0]['day']['chance_precip'] + u"%です．"

	api.PostUpdate(status=weather_Takatsuki)

else:
	tweet_text = "@" + "kensuke_linx" + " " + "Error"
	api.PostUpdate(status=tweet_text)