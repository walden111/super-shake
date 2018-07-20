#!/usr/bin/env python  
# encoding: utf-8  

""" 
@software: PyCharm 
@file: hello.py 
@time: 2018/7/20 1:42 
"""


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return '<h1>hello,%s!</h1>' % (environ['PATH_INFO'][1:] or 'web')


if __name__ == "__main__":
    pass  