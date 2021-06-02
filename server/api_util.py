"""
@project: colour_life
@author: kang 
@github: https://github.com/fsksf 
@since: 2021/5/19 5:35 PM
"""

import os
import inspect
import types
from server import HANDLERS


class OpenApiDecorate:
    """API 装饰器
        name:
    """

    def __init__(self, name=None):
        self.name = name

    def __call__(self, original_func):
        def _api_func(s1, *arg, **kwargs):
            return original_func(s1, *arg, **kwargs)

        _doc = inspect.getdoc(original_func)
        _description = _doc.split("\n")[0] if _doc else ""
        _api_func.__api_description = _description

        return _api_func


def add_handler(path, prefix=None):
    def wp(handler):
        if prefix is not None:
            _path = os.path.join(prefix, path)
        else:
            _path = path
        HANDLERS.append((_path, handler))
        return handler
    return wp
