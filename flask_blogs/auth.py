"""
-------------------------------------------------
   File Name：     auth
   Description :  登陆认证
   Author :       DuanZhangjie
   date：         2021-12-22 16:59
-------------------------------------------------
"""
import functools
from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

# 建立蓝图，url_prefix会添加到所有与本蓝图关联的URL前面
# 蓝图需要在工厂函数里注册
bp = Blueprint('auth', __name__, url_prefix='/auth1')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    return render_template('auth/register.html')

