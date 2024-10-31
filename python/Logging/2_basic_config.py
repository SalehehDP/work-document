import logging

logging.basicConfig(filename='app.log', filemode='a', level=logging.INFO,
                    format='%(name)s - %(levelname)s - %(message)s')


logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

"""output : 
    root - WARNING - This is a warning message
root - ERROR - This is an error message
root - CRITICAL - This is a critical message
root - INFO - This is an info message
root - WARNING - This is a warning message
root - ERROR - This is an error message
root - CRITICAL - This is a critical message


    """
