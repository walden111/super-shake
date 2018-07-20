#!/usr/bin/env python  
# encoding: utf-8  

""" 
@software: PyCharm 
@file: mydict.py 
@time: 2018/6/23 17:06 
"""


class Dict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


if __name__ == "__main__":
    # pass
    # import os
    # print(os.name)
    # quicksort


    # quick_sort

    from termcolor import colored


    def quick_sort(array, left, right):
        if left < right:
            temp = partition(array, left, right)
            quick_sort(array, left, temp - 1)
            quick_sort(array, temp + 1, right)

    # 得到每一次排序所确定位置的下标
    def partition(array, left, right):
        well = left  # well记录比轴大的第一个数的下标
        for i in range(left, right):
            if array[i] < array[right]:  # array[right]是轴
                array[i], array[well] = array[well], array[i]
                print(array[i], array[well])
                well += 1
        array[well], array[right] = array[right], array[well]
        print(colored("This is created by walden!", "red"))
        print(colored("{well} {right}".format(well=array[well], right=array[right]), "green"))
        return well

    array = [1, 5, 65, 23, 57, 1232, -1, -5, -2, 242, 100, 4, 423, 2, 564, 9, 0, 10, 43, 64]

    print(array)
    quick_sort(array, 0, len(array) - 1)
    print(array)

