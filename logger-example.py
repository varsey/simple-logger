import datetime
from Logger import Logger

log_file_name = str(datetime.datetime.now()) + '.log'
logger = Logger(logs_filename=log_file_name)


if __name__ == "__main__":
    logger.log.info('Hello world!')
