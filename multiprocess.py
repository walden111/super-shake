#!/usr/bin/env python  
# encoding: utf-8  

""" 
@software: PyCharm 
@file: multiprocess.py 
@time: 2018/7/12 18:22 
"""


import subprocess
import multiprocessing
import threading

from concurrent.futures import ThreadPoolExecutor


def _main():
    print('At', ctime())

if __name__ == "__main__":
    pass  