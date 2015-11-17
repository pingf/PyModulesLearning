import logging
import traceback


logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', level=logging.DEBUG, datefmt='%m/%d/%Y %I:%M:%S %p')
logging.debug('This message should appear on the console')

class A(object):
    def test(self):
        try:
            raise Exception('WTF!')
        except Exception as e:
            stack = traceback.extract_stack()
            (filename, line, procname, text) = stack[-1]
            context='[loc]'+filename+':'+procname+':'+str(line)
            logging.error('[error]'+str(e)+'  '+context)
a = A()
a.test()
