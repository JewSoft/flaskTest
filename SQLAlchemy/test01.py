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


def delete():
    session.query(UsersTest).filter_by(id=3).delete()
    session.commit()
    session.close()


def sql():
    result = session.query(UsersTest).filter()
    print(result)
    cursor = session.execute(r'select * from userstest where id=1')
    print(cursor.fetchall())
    session.commit()
    session.close()


def add_all():
    session.add_all([
        UsersTest(name='user001', age=21, phone='133'),
        UsersTest(name='user002', age=20, phone='135'),
        UsersTest(name='user003', age=25, phone='139'),
    ])
    session.commit()
    session.close()


def select_all():
    result = session.query(UsersTest).all()
    print(result[1].name)
    result01 = session.query(UsersTest).filter(UsersTest.name == 'USER001').all()
    result02 = session.query(UsersTest).filter(UsersTest.age == 23, UsersTest.name == 'a1').all()
    result03 = session.query(UsersTest).filter(UsersTest.age == 23).first()
    print(result01[0])
    print(result02[0])
    print(result03)
    session.commit()
    session.close()


if __name__ == '__main__':
    # sql()
    # update()
    # insert()
    # delete()
    # add_all()
    select_all()
