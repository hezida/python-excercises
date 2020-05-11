#!/usr/bin/python

from flask import Flask, request

app = Flask("my_app1")

@app.route("/add")
def add():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return 'from flask' + str(a + b)

@app.route("/sub")
def sub():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(a - b)

app.run(port=8000, host="0.0.0.0")