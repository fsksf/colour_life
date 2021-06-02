"""
@project: colour_life
@author: kang 
@github: https://github.com/fsksf 
@since: 2021/6/2 6:03 PM
"""

from server.base_handler import BaseHandler
from server.api_util import add_handler
from server.db import DBUtil

from .model import ElectronicBillboard

PREFIX = 'board'


@add_handler(path='list', prefix=PREFIX)
class BoardListHandler(BaseHandler):

    def get(self):
        DBUtil.select([ElectronicBillboard, ], filter_list=[])


@add_handler(path='info', prefix=PREFIX)
class BoardInfoHandler(BaseHandler):

    def get(self):
        pass

    def post(self):
        pass
