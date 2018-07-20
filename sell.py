#!/usr/bin/env python  
# encoding: utf-8  

""" 
@software: PyCharm 
@file: sell.py 
@time: 2018/6/14 18:12 
"""


def is_year(t):
    if ((t % 4 == 0 and t % 100 != 0) or (t % 400 == 0)):
        return True
    else:
        return False


def get_due_date(order_data):
    due_date = order_data
    if due_date["day"] == 31:
        if due_date["month"] == 7:
            due_date["day"] = 31
        elif due_date["month"] == 1:
            if is_year(due_date["year"]) is True:
                due_date["day"] = 29
            else:
                due_date["day"] = 28
        else:
            due_date["day"] = 30
    elif due_date["day"] == 29 or due_date["day"] == 30:
        if due_date["month"] == 1:
            if is_year(due_date["year"]) is True:
                due_date["day"] = 29
            else:
                due_date["day"] = 28
    else:
        pass
    due_date["month"] = due_date["month"] + 1
    return due_date


if __name__ == "__main__":
    # class Student(object):
    #     def __init__(self):
    #         self.name = 'Michael'
    #
    #     def __getattr__(self, attr):
    #         if attr == 'score':
    #             return 25
    # s = Student()
    # print(s.name)
    # print(s.score)
    class Chain(object):
        def __init__(self, path=''):
            self._path = path

        def __getattr__(self, path):
            return Chain('%s/%s' % (self._path, path))

        def __str__(self):
            return self._path

        # __repr__ == __str__


    str = Chain().status.user.timeline.list
    print(str)