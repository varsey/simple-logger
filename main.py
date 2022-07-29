import datetime
from DicLogger import DicLogger
from LoggerSettings import LoggerSettings

log_file_name = str(datetime.datetime.now()) + '.log'
logger_settings = LoggerSettings(log_file_name)
logger = DicLogger(logger_settings.LOG_SETTINGS)


if __name__ == "__main__":
    while True:
        logger.log.info('Hello world!')
