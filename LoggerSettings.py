class LoggerSettings:
    def __init__(self, log_filename: str):
        self.LOG_SETTINGS = {
            'version': 1,
            'disable_existing_loggers': False,
            'formatters': {
                'default': {
                    'format': '%(asctime)s: %(name)s: #%(lineno)d: %(levelname)s - %(message)s'
                }
            },
            'handlers': {
                "file_handler": {
                    'level': 'DEBUG',
                    'class': 'logging.FileHandler',
                    'formatter': 'default',
                    'filename': log_filename,
                    'encoding': 'utf-8',
                    'mode': 'w',
                },
                "console": {
                    "formatter": "default",
                    "class": "logging.StreamHandler",
                    "level": "DEBUG"
                }
            },
            'loggers': {
                "": {
                    'handlers': ['file_handler', 'console'],
                    'level': 'DEBUG',
                    'propagate': True
                }
            }
        }
