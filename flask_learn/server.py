#!/usr/bin/env python  
# encoding: utf-8  

""" 
@software: PyCharm 
@file: server.py 
@time: 2018/7/20 10:35 
"""
from wsgiref.simple_server import make_server
from hello import application

httpd = make_server('', 8000, application)
print 'Serving HTTP on port 8000...'

httpd.serve_forever()


if __name__ == "__main__":
    pass  