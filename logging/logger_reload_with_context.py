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
        print(stack)

        steps = [mod + ':' + str(line) + ':' + ctx for _, line, mod, ctx in stack[:-3]]
        stack = '>>'.join(steps)
        return '  [loc] ' + filename + ':' + procname + ':' + str(line) + '  [stk] ' + stack

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
    def t1(self):
        self.t2('hello')

    def t2(self, text):
        print(text)
        self.t3('world')

    def t3(self, text):
        print(text)
        self.test()

    def test(self):
        try:
            raise Exception('WTF!')
        except Exception as e:
            logger.error(e)


a = A()
a.t1()
