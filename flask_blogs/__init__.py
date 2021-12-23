"""
-------------------------------------------------
   File Name：     __init__.py
   Description :
   Author :       DuanZhangjie
   date：         2021-12-22 14:42
-------------------------------------------------
"""

# 这个是应用工厂

import os
from flask import Flask
import logging


def create_app(test_config=None):

    # log的配置
    logFile = open('logs/LogTest.log', encoding='utf-8', mode='a+')
    logging.basicConfig(format='%(asctime)s %(levelname)s: %(filename)s %(funcName)s %(message)s',
                        stream=logFile,
                        level=logging.WARNING,
                        datefmt='%Y:%m:%d %H:%M:%S')

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',

        # DATABASE=os.path.join(app.instance_path,'flaskr.sqlite'),
    )
    app.logger.warning('试验LOG')
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    @app.route('/hello')
    def hello():
        return 'Hello,World!'

    # 注册蓝图
    from flask_blogs import auth
    app.register_blueprint(auth.bp)
    return app


# 启动框架在这里启动就可以了
# 其实就是让app=Flask().run就行
if __name__ == '__main__':
    create_app().run(debug=True)
