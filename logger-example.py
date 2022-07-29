import datetime
from Logger import Logger

log_file_name = str(datetime.datetime.now()) + '.log'
l = Logger(logs_filename=log_file_name)

if __name__ == "__main__":
    l.log.info('Hello world!')
