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

        # 在蓝图中使用log，需要用以下语句。记得导包
        # 其实current_app的意思就是获取当前正在执行的flask实例
        # 如果要对当前的flask实例进行操作，也可用这个方法调取
        current_app.logger.debug('这是debug模式')
        current_app.logger.error(f'回传的用户名及密码：{username},{password}')
        current_app.logger.info('这是info模式')
        current_app.logger.warning('这是warning模式')
        # 对密码进行验证，前面是hash值，后面是真实值
        # 对用户密码进行保存的时候应保存为hash值
        if check_password_hash(generate_password_hash('1'), password):
            # 登陆成功后进行session处理
            session.clear()
            session['user_id'] = 10
            g.user = 10
            # 这个url_for里的函数名前要加上蓝图的名称，如果使用了蓝图的话。
            # auth_abc.a的意思是：名称为auth_abc的蓝图下的名称为a的函数
            # return redirect(url_for('auth_abc.a'))
            return redirect(url_for('blog.index'))
        else:
            g.user = None

        return f'密码不正确。用户名：{username}，密码hash：{generate_password_hash(password)}'


@bp.route('/')
def a():
    # 校验session
    if 10 == session['user_id']:
        return '校验成功'
    return '校验不存在'
