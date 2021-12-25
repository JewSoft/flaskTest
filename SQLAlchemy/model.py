"""
-------------------------------------------------
   File Name：     test01
   Description :
   Author :       DuanZhangjie
   date：         2021-12-23 20:06
-------------------------------------------------
"""
import datetime
from sqlalchemy import Column, Integer, String, DateTime, UniqueConstraint, Index
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine(
    "mysql+pymysql://*:*@127.0.0.1:3306/djangotest?charset=utf8",
    max_overflow=0,
    pool_size=5,
    pool_timeout=30,
    # pool_recyle=-1
)


class UsersTest(Base):
    __tablename__ = 'userstest'
    id = Column(Integer, primary_key=True)
    # name = Column(String(32), index=True, nullable=False)
    name = Column(String(32), nullable=False)
    age = Column(Integer, nullable=False)
    phone = Column(String(11))
    addr = Column(String(64), nullable=True)
    create_time = Column(DateTime, default=datetime.datetime.now)

    # __table_args__ = (
    #     UniqueConstraint('id', 'name'),
    #     Index('phone', 'addr', unique=True)
    # )

    def __str__(self):
        return f'object:<id:{self.id} name:{self.name}>'


def creat_tb():
    Base.metadata.create_all(engine)


def drop_tb():
    Base.metadata.drop_all(engine)


if __name__ == '__main__':
    drop_tb()
    creat_tb()
