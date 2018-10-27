#!/usr/bin/env python
# encoding: utf-8
from __future__ import absolute_import

import requests


def fetch_request():
    url = 'http://web.sqt.gtimg.cn/q=sh601390'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,cy;q=0.8,zh-TW;q=0.7',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Host': 'web.sqt.gtimg.cn',
        'Pragma': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
    }

    res = requests.get(url, headers=headers)
    tests = res.text.split('~')
    print tests


if __name__ == '__main__':
    fetch_request()
