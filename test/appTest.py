"""
-------------------------------------------------
   File Name：     appTest.py
   Description :  demo试验
   Author :       DuanZhangjie
   date：         2021-12-21 15:46
-------------------------------------------------
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('register.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
