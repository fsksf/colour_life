"""
@project: colour_life
@author: kang 
@github: https://github.com/fsksf 
@since: 2021/5/14 6:50 PM
"""
import enum
from sqlalchemy import Column, Integer, String, BIGINT, Enum, DATETIME
from server.db import Base


class BillboardType(enum.Enum):
    lost_and_found = 0              # 失物招领
    notice_for_Lost = 1             # 寻物启事
    rent = 2                        # 招租
    asking_for_rent = 3             # 求租


class ElectronicBillboard(Base):
    id = Column(BIGINT)
    title = Column(name='title', comment='公告标题', type_=String(50))
    dt = Column(DATETIME, name='dt', comment='发帖时间')
    user_id = Column(Integer, comment='用户id')
    type_ = Column(Enum(BillboardType), comment='所属分类')
    comment = Column(String(1000), comment='内容')
