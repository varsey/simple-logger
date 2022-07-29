from DicLogger import DicLogger
from LoggerSettings import LoggerSettings

logger_settings = LoggerSettings()
logger = DicLogger(logger_settings.LOG_SETTINGS)


if __name__ == "__main__":
    while True:
        logger.log.info('Hello world!')
