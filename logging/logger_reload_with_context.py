import logging
import traceback
from yaml_config import yaml_config

yaml_config('yaml.conf')


class ContextLogger(object):
    def __init__(self, name):
        self.logger = logging.getLogger(name)

    def _context(self):
        stack = traceback.extract_stack()
        (filename, line, procname, text) = stack[-3]
        return '  [loc] ' + filename + ':' + procname + ':' + str(line)

    def critical(self, msg):
        self.logger.critical('[msg] ' + str(msg) + self._context())

    def error(self, msg):
        self.logger.error('[msg] ' + str(msg) + self._context())

    def warning(self, msg):
        self.logger.warning('[msg] ' + str(msg) + self._context())

    def info(self, msg):
        self.logger.info('[msg] ' + str(msg) + self._context())

    def debug(self, msg):
        self.logger.debug('[msg] ' + str(msg) + self._context())


logger = ContextLogger('root')  # logging.getLogger('test')


class A(object):
    def test(self):
        try:
            raise Exception('WTF!')
        except Exception as e:
            logger.error(e)


a = A()
a.test()
