#coding:utf-8
"""
Copyright (c) 2014. Kensuke Kousaka

This software is released under the MIT License

http://opensource.org/licenses/mit-license.php
"""
__author__ = 'Kensuke Kousaka'

import twitter
import t_key


def main():
    # 認証鍵の取得
    api_key = t_key.consumer_key
    api_secret = t_key.consumer_secret
    access_token_key = t_key.access_token
    access_token_secret = t_key.access_token_secret

    # 認証鍵を使ってOAuth認証を行い，APIを叩けるようにする
    api = twitter.Api(api_key, api_secret, access_token_key, access_token_secret)

    return api

if __name__ == '__main__':
    main()