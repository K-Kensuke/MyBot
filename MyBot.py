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

    elif 'Wakeup' in argv[1]:
        tweet_text = "@" + "kensuke_linx" + " " + u"6時です．もうそろそろ起きよう．"

        api.PostUpdate(status=tweet_text)

    elif 'Weather' in argv[1]:  # 天気情報を取得（神戸と高槻）
        result_kobe = pywapi.get_weather_from_weather_com('JAXX0040')
        result_takatsuki = pywapi.get_weather_from_weather_com('JAXX0083')

        if 'Today' in argv[2]:
            if 'Day' in argv[3]:
                weather_kobe = "@" + "kensuke_linx" + " " + u"今日の日中の神戸は" \
                               + result_kobe['forecasts'][0]['day']['text'] + u"，気温は" \
                               + result_kobe['forecasts'][0]['low'] + u"~" + result_kobe['forecasts'][0]['high'] \
                               + u"℃，湿度は" + result_kobe['forecasts'][0]['day']['humidity'] + u"%，降水確率は" \
                               + result_kobe['forecasts'][0]['day']['chance_precip'] + u"%だよ．"

                api.PostUpdate(status=weather_kobe)

                weather_takatsuki = "@" + "kensuke_linx" + " " + u"今日の日中の高槻は" \
                                    + result_takatsuki['forecasts'][0]['day']['text'] + u"，気温は" \
                                    + result_takatsuki['forecasts'][0]['low'] + u"~" + result_takatsuki['forecasts'][0]['high'] \
                                    + u"℃，湿度は" + result_takatsuki['forecasts'][0]['day']['humidity'] + u"%，降水確率は" \
                                    + result_takatsuki['forecasts'][0]['day']['chance_precip'] + u"%だよ．"

                api.PostUpdate(status=weather_takatsuki)

            elif 'Night' in argv[3]:
                weather_kobe = "@" + "kensuke_linx" + " " + u"今日の夜の神戸は" \
                               + result_kobe['forecasts'][0]['night']['text'] + u"，気温は" \
                               + result_kobe['forecasts'][0]['low'] + u"~" + result_kobe['forecasts'][0]['high'] \
                               + u"℃，湿度は" + result_kobe['forecasts'][0]['night']['humidity'] + u"%，降水確率は" \
                               + result_kobe['forecasts'][0]['night']['chance_precip'] + u"%だよ．"

                api.PostUpdate(status=weather_kobe)

                weather_takatsuki = "@" + "kensuke_linx" + " " + u"今日の夜の高槻は" \
                                    + result_takatsuki['forecasts'][0]['night']['text'] + u"，気温は" \
                                    + result_takatsuki['forecasts'][0]['low'] + u"~" + result_takatsuki['forecasts'][0]['high'] \
                                    + u"℃，湿度は" + result_takatsuki['forecasts'][0]['night']['humidity'] + u"%，降水確率は" \
                                    + result_takatsuki['forecasts'][0]['night']['chance_precip'] + u"%だよ．"

                api.PostUpdate(status=weather_takatsuki)

        elif 'Tomorrow' in argv[2]:
            if 'Day' in argv[3]:
                weather_kobe = "@" + "kensuke_linx" + " " + u"明日の日中の神戸は" \
                               + result_kobe['forecasts'][1]['day']['text'] + u"，気温は" \
                               + result_kobe['forecasts'][1]['low'] + u"~" + result_kobe['forecasts'][1]['high'] \
                               + u"℃，湿度は" + result_kobe['forecasts'][1]['day']['humidity'] + u"%，降水確率は" \
                               + result_kobe['forecasts'][1]['day']['chance_precip'] + u"%だよ．"

                api.PostUpdate(status=weather_kobe)

                weather_takatsuki = "@" + "kensuke_linx" + " " + u"明日の日中の高槻は" \
                                    + result_takatsuki['forecasts'][1]['day']['text'] + u"，気温は" \
                                    + result_takatsuki['forecasts'][1]['low'] + u"~" + result_takatsuki['forecasts'][1]['high'] \
                                    + u"℃，湿度は" + result_takatsuki['forecasts'][1]['day']['humidity'] + u"%，降水確率は" \
                                    + result_takatsuki['forecasts'][1]['day']['chance_precip'] + u"%だよ．"

                api.PostUpdate(status=weather_takatsuki)

            elif 'Night' in argv[3]:
                weather_kobe = "@" + "kensuke_linx" + " " + u"明日の夜の神戸は" \
                               + result_kobe['forecasts'][1]['night']['text'] + u"，気温は" \
                               + result_kobe['forecasts'][1]['low'] + u"~" + result_kobe['forecasts'][1]['high'] \
                               + u"℃，湿度は" + result_kobe['forecasts'][1]['night']['humidity'] + u"%，降水確率は" \
                               + result_kobe['forecasts'][1]['night']['chance_precip'] + u"%だよ．"

                api.PostUpdate(status=weather_kobe)

                weather_takatsuki = "@" + "kensuke_linx" + " " + u"明日の夜の高槻は" \
                                    + result_takatsuki['forecasts'][1]['night']['text'] + u"，気温は" \
                                    + result_takatsuki['forecasts'][1]['low'] + u"~" + result_takatsuki['forecasts'][1]['high'] \
                                    + u"℃，湿度は" + result_takatsuki['forecasts'][1]['night']['humidity'] + u"%，降水確率は" \
                                    + result_takatsuki['forecasts'][1]['night']['chance_precip'] + u"%だよ．"

                api.PostUpdate(status=weather_takatsuki)

    elif 'Event' in argv[1]:
        if 'Today' in argv[2]:
            # Google Calendar APIを用いて，イベント情報を取得する
            entire_event = getEvent.main(argv, 0)

            tweet_text = "@" + "kensuke_linx" + " " + u"本日のイベントは，" + str(len(entire_event)) + u"件あるよ．"
            api.PostUpdate(status=tweet_text)

            num = 0
            while num < len(entire_event):
                event_item = entire_event[num]
                event_summary = event_item[0]
                event_time = event_item[1]

                tweet_text = "@" + "kensuke_linx" + " " + str(num + 1) + u"件目は" + " " + event_summary + " " + u"で，開始時間は" \
                                 + " " + event_time + " " + u"だよ．"
                api.PostUpdate(status=tweet_text)

                num += 1

        elif 'Tomorrow' in argv[2]:
            # Google Calendar APIを用いて，イベント情報を取得する
            entire_event = getEvent.main(argv, 1)

            tweet_text = "@" + "kensuke_linx" + " " + u"明日のイベントは，" + str(len(entire_event)) + u"件あるよ．"
            api.PostUpdate(status=tweet_text)

            num = 0
            while num < len(entire_event):
                event_item = entire_event[num]
                event_summary = event_item[0]
                event_time = event_item[1]

                tweet_text = "@" + "kensuke_linx" + " " + str(num + 1) + u"件目は" + " " + event_summary + " " + u"で，開始時間は" \
                                 + " " + event_time + " " + u"だよ．"
                api.PostUpdate(status=tweet_text)

                num += 1

    elif 'Shower' in argv[1]:
        tweet_text = "@" + "kensuke_linx" + " " + u"シャワーして目を醒まそう．"

        api.PostUpdate(status=tweet_text)  # 12:50~13:10

    elif 'GoHome' in argv[1]:
        tweet_text = "@" + "kensuke_linx" + " " + u"学校なうなら，そろそろ帰らないと寝られないよ？"

        api.PostUpdate(status=tweet_text)

    elif 'Bath' in argv[1]:
        tweet_text = "@" + "kensuke_linx" + " " + u"就寝1時間前です．そろそろお風呂に入ろう．"

        api.PostUpdate(status=tweet_text)

    elif 'Sleep' in argv[1]:
        tweet_text = "@" + "kensuke_linx" + " " + u"22時です．もうそろそろ寝よう."

        api.PostUpdate(status=tweet_text)

    elif 'Success' in argv[1]:
        now = datetime.datetime.now()
        nowstr = now.strftime('%Y/%m/%d %H:%M:%S')

        tweet_text = "@" + "kensuke_linx" + " " + nowstr + " " + u"Task is complete!"

        api.PostUpdate(status=tweet_text)

    elif 'Failure' in argv[1]:
        now = datetime.datetime.now()
        nowstr = now.strftime('%Y/%m/%d %H:%M:%S')

        tweet_text = "@" + "kensuke_linx" + " " + nowstr + " " + u"Task failed…"

        api.PostUpdate(status=tweet_text)

    elif 'CPUtemp' in argv[1]:
        cputemp = subprocess.check_output("sensors | grep 'Core 0' | awk '{ print $3 }'", shell=True).rstrip()
        decode_cputemp = unicode(cputemp, "utf-8")
        now = datetime.datetime.now()
        nowstr = now.strftime('%Y/%m/%d %H:%M:%S')

        tweet_text = nowstr + u"現在のサーバのCPU温度は，" + decode_cputemp + u"だよ．"

        api.PostUpdate(status=tweet_text)

    elif 'Log' in argv[1]:
        log_text = unicode(argv[2], "utf-8")
        if len(log_text) > 140:
            log_text_list = split_str(log_text, 140)

            for text in log_text_list:
                api.PostUpdate(status=text)
        else:
            tweet_text = log_text
            api.PostUpdate(status=tweet_text)

    elif 'Memory' in argv[1]:
        memory_temp = subprocess.check_output("""free | grep - | awk '{print $3 "-" $4}'""", shell=True).rstrip()
        memory = unicode(memory_temp, "utf-8").split("-")
        now = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')

        tweet_text = now + u"現在のサーバのメモリ使用状況は，" + memory[0] + u"/" + str(int(memory[0]) + int(memory[1])) + u"だよ．"

        api.PostUpdate(status=tweet_text)


def split_str(s, n):
    # Split string by its length
    length = len(s)
    return [s[i:i+n] for i in range(0, length, n)]


if __name__ == '__main__':
    main(sys.argv)