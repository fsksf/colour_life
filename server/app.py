"""
@project: colour_life
@author: kang 
@github: https://github.com/fsksf 
@since: 2021/3/5 11:42 PM
"""
import secrets
import tornado.ioloop
import tornado.web
from server.base_handler import BaseHandler, LoginHandler, LogonHander, MainHandler


settings = {
    "cookie_secret": secrets.token_urlsafe(30),
    "login_url": "/login",
}


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/login", LoginHandler),
        (r"/logon", LogonHander)
    ], **settings)
