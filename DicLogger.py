import logging.config


class DicLogger:
    LOG_FORMAT = '%(asctime)-15s %(name)s %(levelname)-8s %(message)s'

    def __init__(self, log_settings: dict):
        logger = logging.getLogger(__name__)
        logging.config.dictConfig(log_settings)
        self.log = logger
