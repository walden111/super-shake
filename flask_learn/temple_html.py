#!/usr/bin/env python
# encoding: utf-8

"""
@software: PyCharm
@file: temple_html.py
@time: 2018/7/20 13:49
"""


from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/', methods=['GET,POST'])
def home():
    return render_template('home.html')


@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')


@app.route('/signin', methods=['POST'])
def signin():
    usename = request.form['usename']
    password = request.form['password']
    if usename == "admin" and password == "password":
        return render_template("signin-ok.html", usename=usename)
    return render_template('form.html', message='error,please input right usename or password!!', usename=usename)


if __name__ == "__main__":
    # pass
    app.run()