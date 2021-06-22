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

PREFIX = '/api/board'

add_api = add_handler(PREFIX)

@add_api(path='list')
class BoardListHandler(BaseHandler):

    def get(self):
        self.get_query_argument(name='')
        DBUtil.select([ElectronicBillboard, ], filter_list=[])


@add_api(path='info')
class BoardInfoHandler(BaseHandler):

    def get(self):
        pass

    def post(self):
        pass
