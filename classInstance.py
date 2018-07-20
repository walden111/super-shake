#!/usr/bin/env python  
# encoding: utf-8  

""" 
@software: PyCharm 
@file: classInstance.py 
@time: 2018/5/29 14:52 
"""


def func():
    pass


class Screen(object):

    @property
    def width(self):
        return self.value

    @property
    def height(self):
        return self._value

    @width.setter
    def width(self, value):
        self.value = value

    @height.setter
    def height(self, value):
        self._value = value

    @property
    def resolution(self):
        return self.value * self._value


if __name__ == "__main__":
    s = Screen()
    s.width = 1024
    s.height = 768
    print(s.resolution)