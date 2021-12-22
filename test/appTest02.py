"""
-------------------------------------------------
   File Name：     appTest02
   Description :
   Author :       DuanZhangjie
   date：         2021-12-21 16:12
-------------------------------------------------
"""
from flask import Flask, Markup

app = Flask(__name__)


@app.route('/')
def index():
    return Markup('<div>Hello %s<div>') % '<em>Flask<em>'


if __name__ == '__main__':
    app.run(debug=True)
