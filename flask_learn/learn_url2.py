#!/usr/bin/env python  
# encoding: utf-8  

""" 
@software: PyCharm 
@file: learn_url2.py 
@time: 2018/7/19 16:48 
"""


from flask import Flask, url_for


app = Flask(__name__)


@app.route('item/1/')
def item(id):
    pass


with app.test_request_context():
    print(url_for('item', id='1'))
    print(url_for('item', id=2, next='/'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9000)
