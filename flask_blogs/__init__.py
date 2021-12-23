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
from logging.handlers import RotatingFileHandler
from config import config_map


def create_app(config_name):
    # log的配置
    # logFile = open('logs/LogTest.log', encoding='utf-8', mode='a+')
    # logging.basicConfig(format='%(asctime)s %(levelname)s: %(filename)s %(funcName)s %(message)s',
    #                     stream=logFile,
    #                     level=logging.WARNING,
    #                     datefmt='%Y:%m:%d %H:%M:%S')
    #
    # app = Flask(__name__, instance_relative_config=True)
    # app.config.from_mapping(
    #     SECRET_KEY='dev',
    #
    #     # DATABASE=os.path.join(app.instance_path,'flaskr.sqlite'),
    # )
    # app.logger.warning('试验LOG')
    # if test_config is None:
    #     app.config.from_pyfile('config.py', silent=True)
    # else:
    #     app.config.from_mapping(test_config)
    #
    # @app.route('/hello')
    # def hello():
    #     return 'Hello,World!'

    # 设置日志
    setup_log(config_name)
    # 实例为flask
    app = Flask(__name__)
    # 配置实例
    app.config.from_object(config_map[config_name])

    # 注册蓝图
    from flask_blogs import auth
    app.register_blueprint(auth.bp)
    return app


def setup_log(config_name):

    logging.basicConfig(level=config_map[config_name].LOG_LEVEL)
    file_log_handler = RotatingFileHandler(
        filename='logs/flask.log',
        maxBytes=1024 * 1024 * 20,
        backupCount=10,
        encoding='utf-8',
        mode='a+'
    )
    formatter = logging.Formatter('%(asctime)s %(levelname)s: %(filename)s %(funcName)s %(message)s')
    file_log_handler.setFormatter(formatter)
    logging.getLogger().addHandler(file_log_handler)


# 启动框架在这里启动就可以了
# 其实就是让app=Flask().run就行
if __name__ == '__main__':
    # 如果要切换配置，只需要修改create_app()函数中的参数即可。
    # 可以方便的进行全局切换
    create_app('development').run()
