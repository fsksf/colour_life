"""
@project: colour_life
@author: kang 
@github: https://github.com/fsksf 
@since: 2021/3/5 11:43 PM
"""
import tornado.ioloop
from server.app import make_app

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()