"""
-------------------------------------------------
   File Name：     test03
   Description :
   Author :       DuanZhangjie
   date：         2021-12-21 17:21
-------------------------------------------------
"""
from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


with app.test_request_context():
    print(url_for('index'))
# if __name__ == '__main__':
#     app.run(debug=True)
