#!/usr/bin/env python
# encoding: utf-8

"""
@software: PyCharm
@file: bsscrape.py
@time: 2018/3/19 15:27
"""

import urllib2
import download
from bs4 import BeautifulSoup


# def bsscrape(url):
def bsscrape(html):

    # html = download.download(url)
    soup = BeautifulSoup(html, "lxml")

    ul = soup.find('ul', attrs={'class': 'nav pull-right'})
    return  ul

if __name__ == "__main__":

    url = "http://example.webscraping.com/view/United-Kingdom-239"
    html = urllib2.urlopen(url).read()
    info = bsscrape(html)
    print info