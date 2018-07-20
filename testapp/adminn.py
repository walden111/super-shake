#!/usr/bin/env python  
# encoding: utf-8  

""" 
@software: PyCharm 
@file: adminn.py 
@time: 2018/7/3 15:05 
"""

from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()


if __name__ == "__main__":
    pass  