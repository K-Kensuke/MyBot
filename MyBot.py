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
import getEvent

import sys

import subprocess


def main(argv):
    # Twitter APIにアクセスできるように認証を行う
    api = authtwitter.main()

    if 'Login' in argv[1]:
        now = datetime.datetime.today()
        tweet_text = "@" + "kensuke_linx" + " " + "'" + argv[2] + "'" + " " + "has logged in from" + " " \
                     + argv[3] + " " + "at" + " " + now.strftime("%Y-%m-%d %H:%M:%S")

        api.PostUpdate(status=tweet_text)

    # 6:00
    elif 'Wakeup' in argv[1]:
        tweet_text = "@" + "kensuke_linx" + " " + u"6時です．もうそろそろ起きよう．"

        # Tweetする
        api.PostUpdate(status=tweet_text)

    # 6:30
    elif 'WeatherAndEvent' in argv[1]:  # 天気情報を取得（神戸と高槻）
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

        # Google Calendar APIを用いて，イベント情報を取得する
        entireEvent = getEvent.main(argv)


        # イベント情報を呟く
        tweet_text = "@" + "kensuke_linx" + " " + u"本日のイベントは，" + str(len(entireEvent)) + u"件あります．"
        api.PostUpdate(status=tweet_text)

        num = 0
        while num < len(entireEvent):
            eventItem = entireEvent[num]
            eventSummary = eventItem[0]
            eventTime = eventItem[1]

            tweet_text = "@" + "kensuke_linx" + " " + str(num + 1) + u"件目は" + " " + eventSummary + " " + u"で，開始時間は" \
                         + " " + eventTime + " " + u"です．"
            api.PostUpdate(status=tweet_text)

            num += 1

    # 6:45
    elif 'Shower' in argv[1]:
        tweet_text = "@" + "kensuke_linx" + " " + u"シャワーして目を醒まそう"

        api.PostUpdate(status=tweet_text)  # 12:50~13:10

    # 21:00
    elif 'Bath' in argv[1]:
        tweet_text = "@" + "kensuke_linx" + " " + u"就寝1時間前です．そろそろお風呂に入ろう．"

        # Tweetする
        api.PostUpdate(status=tweet_text)

    # # 21:30
    # elif 'BeforeSleep' in argv[1]:
    #     tweet_text = "@" + "kensuke_linx" + " " + u"電子機器の電源をすべて切って，寝るだけにしよう．"
    #
    #     # Tweetする
    #     api.PostUpdate(status=tweet_text)

    # 22:00
    elif 'Sleep' in argv[1]:
        tweet_text = "@" + "kensuke_linx" + " " + u"22時です．もうそろそろ寝よう."

        # Tweetする
        api.PostUpdate(status=tweet_text)

    elif 'Success' in argv[1]:
        tweet_text = "@" + "kensuke_linx" + " " + u"Task is complete!"

        api.PostUpdate(status=tweet_text)

    elif 'Failure' in argv[1]:
        tweet_text = "@" + "kensuke_linx" + " " + u"Task failed"

        api.PostUpdate(status=tweet_text)

    elif 'CPUtemp' in argv[1]:
        cputemp = subprocess.check_output("sensors | grep 'Core 0' | awk '{ print $3 }'", shell=True)
        decode_cputemp = unicode(cputemp, "utf-8")

        tweet_text = "@" + "kensuke_linx" + " " + u"現在のサーバのCPU温度は，" + decode_cputemp + u"です．"

        api.PostUpdate(status=tweet_text)


if __name__ == '__main__':
    main(sys.argv)