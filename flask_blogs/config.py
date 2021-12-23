"""
-------------------------------------------------
   File Name：     config
   Description :   配置文件
   Author :       DuanZhangjie
   date：         2021-12-23 15:36
-------------------------------------------------
"""
import logging


class MyConfig:
    """
    配置的基础类
    """

    DEBUG = True
    LOG_LEVEL = logging.DEBUG

    SECRET_KEY = 'abc'

    # SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/flask_job_project"
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    # REDIS_HOST = '127.0.0.1'
    # REDIS_PORT = 6379


class ProductionConfig(MyConfig):
    DEBUG = False
    LOG_LEVEL = logging.ERROR


class DevelopmentConfig(MyConfig):
    pass


config_map = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
