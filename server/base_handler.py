"""
@project: colour_life
@author: kang 
@github: https://github.com/fsksf 
@since: 2021/5/14 7:33 PM
"""
from abc import ABC
from typing import Optional, Awaitable
import json
import tornado
import tornado.web
import tornado.escape

from .db import DBUtil
from .model import User
from .api_util import add_handler
from .logger import sys_logger


class BaseHandler(tornado.web.RequestHandler, ABC):
    
    def __init__(self, *args, **kwargs):
        self._json_body_arguments: dict = dict()
        super(BaseHandler, self).__init__(*args, **kwargs)
        if self.request.headers.get('Content-Type', '').startswith('application/json'):
            self.parse_json_body_to_dict()
    
    def get_current_user(self):
        return self.get_secure_cookie("user")

    def get_json_body_argument(self, key, default=None):
        return self._json_body_arguments.get(key, default)
    
    def parse_json_body_to_dict(self):
        self._json_body_arguments.update(json.loads(self.request.body.decode('utf-8')))


@add_handler(path=r'/', prefix='/api')
class MainHandler(BaseHandler):
    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    def get(self):
        if not self.current_user:
            self.redirect("/login")
            return
        name = tornado.escape.xhtml_escape(self.current_user)
        self.write("Hello, " + name)


@add_handler(path=r'/logon', prefix='/api')
class LogonHander(BaseHandler):

    def post(self):
        name = self.get_body_argument('name')
        password = self.get_body_argument('password')

        DBUtil.insert(User, [{'name': name, 'password': password}])
        self.redirect('/login')

    def get(self):
        self.write('<html><body><form action="/logon" method="post">'
                   'Name: <input type="text" name="name">'
                   'Password: <input type="text" name="password">'
                   '<input type="submit" value="Sign on">'
                   '</form></body></html>')


@add_handler(path=r'/login', prefix='/api')
class LoginHandler(BaseHandler):

    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    def get(self):
        self.write('<html><body><form action="/login" method="post">'
                   'Name: <input type="text" name="name">'
                   'Password: <input type="text" name="password">'
                   '<input type="submit" value="Sign in">'
                   '</form></body></html>')

    def post(self):
        code = self.get_json_body_argument('code')
        password = self.get_json_body_argument('password')
        sys_logger.info(f'user login with code: {code}')
        user = DBUtil.select(query_list=[User], filter_list=[User.code == code])
        if user:
            if user[0].password == password:
                self.set_secure_cookie("user", code)
                self.redirect("/")
                return
        self.write("password error")


@add_handler(path=r'/about', prefix='/api')
class AboutHandler(BaseHandler):
    def get(self):
        sys_logger.info('about page')
        self.write('about!')
