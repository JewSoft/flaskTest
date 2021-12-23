"""
-------------------------------------------------
   File Name：     test01
   Description :
   Author :       DuanZhangjie
   date：         2021-12-23 20:23
-------------------------------------------------
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from model import *

Session = sessionmaker(bind=engine)
session = scoped_session(Session)


def insert():
    user_obj = UsersTest(name='a1', phone='123', age=23, addr='China')
    session.add(user_obj)
    session.commit()
    session.close()


def update():
    session.query(UsersTest).filter_by(id=1).update({'name': 'USER001'})
    session.query(UsersTest).filter_by(id=2).update(
        {'addr': UsersTest.addr + 'Beijing'}, synchronize_session=False)
    session.commit()
    session.close()


def sql():
    result = session.query(UsersTest).filter()
    print(result)
    cursor = session.execute(r'select * from userstest where id=1')
    print(cursor.fetchall())
    session.commit()
    session.close()


if __name__ == '__main__':
    sql()
