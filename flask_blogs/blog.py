"""
-------------------------------------------------
   File Name：     blog
   Description :
   Author :       DuanZhangjie
   date：         2021-12-23 17:21
-------------------------------------------------
"""
import functools
from flask import Blueprint
from flask import Flask
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from flask import current_app

bp = Blueprint('blog', __name__)


@bp.route('/')
def index():
    # if g.user is None:
    #     return f'校验成功，{g.user}'
    # return '校验不存在'
    if 10 == session['user_id']:
        return '校验成功'
    return '校验不存在'
