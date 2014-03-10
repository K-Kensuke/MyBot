#MyBot
TwitterのBot（@kensuke_lynx）．

@kensuke_linxに対して，特定の時間帯にリプライを送る．cronによる起動が前提．

cronで起動された後，現在時刻を取得・加工したものを利用して，Tweet内容の分岐を行う．

##Library
* python-twitter : [https://code.google.com/p/python-twitter/](https://code.google.com/p/python-twitter/)
  * simplejson : [https://pypi.python.org/pypi/simplejson](https://pypi.python.org/pypi/simplejson)
  * httplib2 : [https://github.com/jcgregorio/httplib2](https://github.com/jcgregorio/httplib2)
  * python-oauth2 : [https://github.com/simplegeo/python-oauth2](https://github.com/simplegeo/python-oauth2)

* python-weather-api : [https://code.google.com/p/python-weather-api/](https://code.google.com/p/python-weather-api/)

##Auther
Kensuke Kousaka（@kensuke_linx）

##License
This software is released under the **MIT License**, see LICENSE.txt