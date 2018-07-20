#!/usr/bin/env python  
# encoding: utf-8  

""" 
@software: PyCharm 
@file: app.py 
@time: 2018/7/20 10:49 
"""


from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>home</h1>'


@app.route('/signin', methods=['GET'])
def signin_form():
    return """<form action='/signin' method="post">
            <p><input name="usename"></p>
            <p><input name="passwd" type="password"></p>
            <p><button type="submit">Sign in</button></p>
            </form>"""


@app.route('/signin', methods=['POST'])
def signin():
    if request.form['usename'] == 'admin' and request.form['passwd'] == 'passwd':
        return '<h1>hello,walden!!</h1>'
    return '<h1>error,please input right usename or password!!</h1>'


if __name__ == "__main__":
    # pass
    app.run()