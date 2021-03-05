"""
@project: colour_life
@author: kang 
@github: https://github.com/fsksf 
@since: 2021/3/5 11:42 PM
"""
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])
