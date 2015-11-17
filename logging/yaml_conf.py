import logging
from yaml_config import yaml_config

yaml_config('yaml.conf')

logger = logging.getLogger('root')
# you have to define root explicitly when using dictConfig
# or define root handler from the top
logger.debug('hello %s', 'world')
