#!/usr/bin/env python  
# encoding: utf-8  

""" 
@software: PyCharm 
@file: sitemap.py 
@time: 2018/3/19 14:54 
"""
import download
import re


def claw_sitemap(url):
    sitemap = download.download(url)
    links = re.findall('<body>(.*?)</body>', sitemap)
    print(links)
    for link in links:
        html = download.download(link)


if __name__ == "__main__":
    # url = "http://example.webscraping.com/view/1"
    # claw_sitemap(url)
    # dict1 = {"walden": 123, "sweety": 234}
    # for key, value in dict1.items():
    #     print(key, value)
    # # print(dict1.items())
    # del dict1['walden']
    # print(dict1)


    # 判断素数
    # def get_prime(from_num, to_num):
    #     prime_list = []
    #     for i in range(from_num, to_num):
    #         for j in range(0, i):
    #             if i % j == 0 or i % 2 == 0:
    #                 prime_list.append(i)

