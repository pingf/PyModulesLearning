import logging
import logging.config

logging.config.fileConfig('file.conf')

# create logger
logger = logging.getLogger('simpleExample')

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')

# Note The fileConfig() API is older than the dictConfig() API and does not provide functionality to cover certain aspects of logging.
# For example, you cannot configure Filter objects, which provide for filtering of messages beyond simple integer levels, using fileConfig().
# If you need to have instances of Filter in your logging configuration, you will need to use dictConfig().
# Note that future enhancements to configuration functionality will be added to dictConfig(),
# so it’s worth considering transitioning to this newer API when it’s convenient to do so.
