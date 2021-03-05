"""
@project: colour_life
@author: kang 
@github: https://github.com/fsksf 
@since: 2021/3/5 11:27 PM
"""
import datetime
import sys
import logbook
from logbook import StreamHandler


DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S.%f"


def get_logger(datetime_func=datetime.datetime.now, log_type='', level='INFO'):

    def logger_formatter(record, handler):
        if level == 'DEBUG':
            prefix = f'{log_type}:{str(record.lineno)}'
        else:
            prefix = f'{log_type}:{record.module}:{str(record.lineno)}'

        log_str = '{dt} {level}: [{prefix}]: {msg}'.format(
            dt=datetime_func().strftime(DATETIME_FORMAT),
            level=record.level_name,
            prefix=prefix,
            msg=record.message
        )

        return log_str
    if level == 'DEBUG':
        logger = logbook.Logger('[system] ', level=logbook.DEBUG)
    else:
        logger = logbook.Logger('[system] ', level=logbook.INFO)
    handler = StreamHandler(sys.stdout)
    handler.formatter = logger_formatter
    logger.handlers = [handler, ]
    return logger


sys_logger = get_logger()