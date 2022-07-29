import os
import sys
import logging


class Logger:
    LOG_FORMAT = '%(asctime)-15s %(name)s %(levelname)-8s %(message)s'

    def __init__(self, logs_filename: str = 'logs.txt'):
        logger_name = os.uname().nodename
        logger = logging.getLogger(logger_name)
        logging.basicConfig(filename=logs_filename, encoding='utf-8', level=logging.INFO, format=self.LOG_FORMAT)
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(logging.Formatter(self.LOG_FORMAT))
        logger.addHandler(handler)
        self.logs_file = logs_filename
        self.log = logger
