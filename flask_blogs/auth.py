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
'''
第一个参数：'auth',蓝图的名称
第二个参数：__name__,蓝图在哪里定义的
第三个参数：url_prefix='/auth',这个蓝图关联的URL前会自动加上/auth
'''
bp = Blueprint('auth_abc', __name__, url_prefix='/auth')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    return render_template('auth/login.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username)
        print(password)

        # 对密码进行验证，前面是hash值，后面是真实值
        # 对用户密码进行保存的时候应保存为hash值
        if check_password_hash(generate_password_hash('1'), password):
            session.clear()
            session['user_id']='user_session'
            return redirect(url_for('index'))

        return f'密码不正确。用户名：{username}，密码hash：{generate_password_hash(password)}'
