import logging
import traceback
from yaml_config import yaml_config

yaml_config('yaml.conf')


class ContextLogger(object):
    USELESS_STACK = -3

    def __init__(self, name, project_path=None):
        self.logger = logging.getLogger(name)
        self.path = project_path

    def _context(self, more=False):
        stack = traceback.extract_stack()
        (filename, line, procname, text) = stack[self.USELESS_STACK]
        filename = self._filename(filename)
        steps = [self._filename(filename) + ':' + str(line) + '#' + mod + ':' + ctx
                 for filename, line, mod, ctx in stack[:self.USELESS_STACK]]
        stack = '  '.join(steps)
        context = '  [loc] ' + filename + ':' + procname + ':' + str(line)
        return context + '  [stk] ' + stack if more else context

    def _filename(self, filename):
        if self.path is not None and filename.find(self.path) > -1:
            if self.path == '/':
                return filename[filename.rfind('/') + 1:]
            else:
                filename = filename[len(self.path):]
                return filename[1:] if filename.find('/') == 0 else filename

    def critical(self, msg):
        self.logger.critical('[msg] ' + str(msg) + self._context(1))

    def error(self, msg):
        self.logger.error('[msg] ' + str(msg) + self._context(1))

    def warning(self, msg):
        self.logger.warning('[msg] ' + str(msg) + self._context())

    def info(self, msg):
        self.logger.info('[msg] ' + str(msg) + self._context())

    def debug(self, msg):
        self.logger.debug('[msg] ' + str(msg) + self._context())


logger = ContextLogger('root', '/')


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
            logger.critical(e)
            logger.error(e)
            logger.warning(e)
            logger.info(e)
            logger.debug(e)


a = A()
a.t1()
