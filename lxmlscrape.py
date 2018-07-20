#!/usr/bin/env python  
# encoding: utf-8  

""" 
@software: PyCharm 
@file: lxmlscrape.py 
@time: 2018/3/19 15:40 
"""

import urllib
import lxml.html as lh
import time


def lxmlscrape(html):
    start = time.time()
    tree = lh.fromstring(html)

    td = tree.cssselect('<body>(.*?)</body>')
    area = td.text_content()
    end = time.time()
    t = end - start
    print(t)
    # print "usetime:%s", t
    return area


if __name__ == '__main__':
    def fabonacci(n):
        """

        :param n:
        :return:
        """
        if n < 2:
            return n
        else:
            return fabonacci(n-2) + fabonacci(n-1)

    # for i in range(0, 20):
    #     b = fabonacci(i)
    #     print(b)

    b = map(lambda x: fabonacci(x), [i for i in range(10)])
    print(list(b))