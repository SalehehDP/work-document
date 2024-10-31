import logging

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')


"""output:
WARNING: root: This is a warning message
ERROR: root: This is an error message
CRITICAL: root: This is a critical message
"""
