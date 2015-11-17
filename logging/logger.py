import logging

logger = logging.getLogger('logger_1')
logger.warning('warning')

stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s:%(message)s')
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

logger.warning('warning again')

root = logging.getLogger()
stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s:%(message)s')
stream_handler.setFormatter(formatter)
root.addHandler(stream_handler)
root.warning('warning')
