"""
@project: colour_life
@author: kang 
@github: https://github.com/fsksf 
@since: 2021/5/14 7:33 PM
"""
from abc import ABC
from typing import Optional, Awaitable

import tornado
import tornado.web
import tornado.escape

from .db import DBUtil
from .model import User


class BaseHandler(tornado.web.RequestHandler, ABC):
    def get_current_user(self):
        return self.get_secure_cookie("user")


class MainHandler(BaseHandler):
    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    def get(self):
        if not self.current_user:
            self.redirect("/login")
            return
        name = tornado.escape.xhtml_escape(self.current_user)
        self.write("Hello, " + name)


class LogonHander(BaseHandler):

    def post(self):
        name = self.get_body_argument('name')
        password = self.get_body_argument('password')

        DBUtil.insert(User, {User.name: name, User.password: password})

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
        name = self.get_body_argument('name')
        password = self.get_body_argument('password')
        user = DBUtil.select(query_list=[User], filter_list=[User.name == name])
        if user:
            if user[0]['password'] == password:
                self.set_secure_cookie("user", self.get_argument("name"))
                self.redirect("/")
        return "password error"