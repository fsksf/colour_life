"""
@project: colour_life
@author: kang 
@github: https://github.com/fsksf 
@since: 2021/5/14 7:40 PM
"""
import enum
from sqlalchemy import Column, Integer, String, BIGINT, Enum, Index
from server.db import Base


class Sex(enum.Enum):
    male = 0
    female = 1
    secret = 2


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(30), comment='登录id')
    name = Column(String(30), comment='昵称')
    password = Column(String(100), comment='密钥')
    phone = Column(String(11), comment='电话')
    sex = Column(Enum(Sex), comment='性别')
    wechat_code = Column(String(30), comment='绑定微信')


Index('ix_user_phone', User.phone)
Index('ix_user_wechat', User.wechat_code)
