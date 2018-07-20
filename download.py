#!/usr/bin/env python  
# encoding: utf-8  

""" 
@software: PyCharm 
@file: download.py
@time: 2018/3/11 22:47 
"""

import urllib


def download(url, user_agent='wswp', num_retries=2):
    print("Downloading:", url)
    headers = {'user-agent': user_agent}
    requset = urllib.Request(url, headers=headers)
    try:
        html = urllib.urlopen(requset).read()
    except urllib.URLError as e:
        print("Download error：", e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, num_retries - 1)
    return html


if __name__ == "__main__":

    # url = "https://www.panda.tv"
    url = "https://www.meetup.com"
    # url = "http://httpstat.us/500"
    download(url)
