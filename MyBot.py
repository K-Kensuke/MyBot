#coding:utf-8
"""
Copyright (c) 2014. Kensuke Kousaka

This software is released under the MIT License

http://opensource.org/licenses/mit-license.php
"""
__author__ = 'Kensuke Kousaka'

import datetime
import pywapi
import authtwitter

import sys


def main(argv):
    # Twitter APIにアクセスできるように認証を行う
    api = authtwitter.main()

    if argv[1] is not None:
        if 'login' in argv[1]:
            now = datetime.datetime.today()
            tweet_text = "@" + "kensuke_linx" + " " + argv[2] + " " + 'has logged in from' + " " + argv[3] + " " \
                         + 'at' + now.strftime("%Y-%m-%d %H:%M:%S")

            api.PostUpdate(status=tweet_text)

    # 現在時刻を取得する
    hour = datetime.datetime.today().hour
    minute = datetime.datetime.today().minute

    hour_string = str(hour)

    # minuteが1桁の場合
    if minute < 10:
        minute_string = '0' + str(minute)
    # minuteが2桁の場合
    else:
        minute_string = str(minute)

    time = int(hour_string + minute_string)

    # 5:50~6:10
    if 550 < time < 610:
        tweet_text = "@" + "kensuke_linx" + " " + u"6時です．もうそろそろ起きよう．"

        # Tweetする
        api.PostUpdate(status=tweet_text)

    # 6:20~6:40
    elif 620 < time < 640:  # 天気情報を取得（神戸と高槻）
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

    # 6:35~6:55
    elif 635 < time < 655:
        tweet_text = "@" + "kensuke_linx" + " " + u"シャワーして目を醒まそう"

        api.PostUpdate(status=tweet_text)  # 12:50~13:10

    # 20:50~21:10
    elif 2050 < time < 2110:
        tweet_text = "@" + "kensuke_linx" + " " + u"就寝1時間前です．そろそろお風呂に入ろう．"

        # Tweetする
        api.PostUpdate(status=tweet_text)

    # 21:20~21:40
    elif 2120 < time < 2140:
        tweet_text = "@" + "kensuke_linx" + " " + u"電子機器の電源をすべて切って，寝るだけにしよう．"

        # Tweetする
        api.PostUpdate(status=tweet_text)

    # 21:50~22:10
    elif 2150 < time < 2210:
        tweet_text = "@" + "kensuke_linx" + " " + u"22時です．もうそろそろ寝よう."

        # Tweetする
        api.PostUpdate(status=tweet_text)

    else:
        tweet_text = "@" + "kensuke_linx" + " " + "Error"
        api.PostUpdate(status=tweet_text)


if __name__ == '__main__':
    main(sys.argv)