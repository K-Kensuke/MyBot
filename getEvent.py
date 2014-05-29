#coding:utf-8
"""
Copyright (c) 2014. Kensuke Kousaka

This software is released under the MIT License

http://opensource.org/licenses/mit-license.php
"""
__author__ = 'Kensuke Kousaka'

import gflags
import httplib2
import codecs
import sys
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage
from oauth2client.tools import run
from apiclient.discovery import build

import t_key

import datetime


def main(argv):
    service = getservice(argv)

    # dateで本日の日付を拾得
    # 表示したい日付は，ここでイジれる（timedeltaに0を渡すと今日のイベント表示，1だと明日…）
    now = datetime.date.today() + datetime.timedelta(0)

    # dateをstringに変換
    nowstr = now.strftime('%Y-%m-%d')

    # Returns entries on the user's calendar list.
    calendars = service.calendarList().list().execute()

    entireEvent = getevent(nowstr, service, calendars)
    return entireEvent


def getservice(argv):
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
    try:
        argv = gflags.FLAGS(argv)
    except gflags.FlagsError, e:
        print ""
        sys.exit()

    storage = Storage('calendar.dat')
    credentials = storage.get()
    if not credentials or credentials.invalid:
        flow = OAuth2WebServerFlow(
            client_id=t_key.client_id,
            client_secret=t_key.client_secret,
            scope=['https://www.googleapis.com/auth/calendar'],
            user_agent='TwitterBot/1.0'
        )
        credentials = run(flow, storage)

    http = httplib2.Http()
    credentials.authorize(http)
    service = build('calendar', 'v3', http=http)
    return service


def getevent(nowstr, service, calendars):
    eventDict = {}

    # パラメータリスト https://developers.google.com/google-apps/calendar/v3/reference/events/list?hl.ja
    # singleEventsクエリをTrueにすることで，繰り返しの予定をバラして表示する
    for calendar in calendars['items']:
        events = service.events().list(calendarId=calendar['id'], singleEvents=True, orderBy='startTime').execute()

        for event in events['items']:
            # event内にsummaryがあった場合
            if 'summary' in event:
                # eventのstartをeventStartに入れる
                eventStart = event['start']

                # eventStart内にdateTimeがあった場合
                if 'dateTime' in eventStart:
                    start = eventStart['dateTime'].split('T')
                    startdate = start[0]
                    starttime = start[1]
                # eventStart内にdateTimeがなかった場合
                else:
                    startdate = eventStart['date']

                eventEnd = event['end']

                if 'dateTime' in eventEnd:
                    end = eventEnd['dateTime'].split('T')
                    enddate = end[0]
                else:
                    enddate = eventEnd['date']

                # 文字列から日付に変換
                tdatetime = datetime.datetime.strptime(startdate, '%Y-%m-%d')
                tStartDate = datetime.date(tdatetime.year, tdatetime.month, tdatetime.day)

                tdatetime = datetime.datetime.strptime(enddate, '%Y-%m-%d')
                tEndDate = datetime.date(tdatetime.year, tdatetime.month, tdatetime.day)

                diffDate = (tEndDate - tStartDate).days

                if diffDate == 0:
                    if nowstr in startdate:
                        if starttime is not None:
                            eventDict[event['summary']] = starttime
                else:
                    num = 0
                    while num <= diffDate:
                        tmp = tStartDate + datetime.timedelta(days=num)
                        tmpstr = tmp.strftime('%Y-%m-%d')

                        if nowstr in tmpstr:
                            if starttime is not None:
                                eventDict[event['summary']] = starttime
                        num += 1

    entireEvent = eventDict.items()
    return entireEvent


if __name__ == '__main__':
    main(sys.argv)