# -*-conding:utf-8-*-
import logging
import time

LEVELS = {'debug':logging.DEBUG,'info':logging.INFO,'warning':logging.WARNING,'error':logging.ERROR,'ceritical':logging.CRITICAL}


logger = logging.getLogger()
logger.setLevel(LEVELS['debug'])

class MyLog:
    # path = os.path.dirname(os.path.dirname(os.path.realpath('__file__')))  #在执行测试案例的文件的时候，这个path的os.path.realpath('__file__')是测试文件，
    # print("ssssssssssssssss{}".format(path))
    path = 'D:\\Users\\tina.gong\\PycharmProjects\\untitled'
    date = time.strftime('%Y-%m-%d %H-%M-%S',time.localtime(time.time()))
    log_file = path + '\\Log\\' + date + '.log'

    fh = logging.FileHandler(log_file,encoding='utf-8')
    ch = logging.StreamHandler()

    formatter = logging.Formatter('%(asctime)s：%(levelname)s-%(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)



    @staticmethod
    def debug(msg):
        logger.addHandler(MyLog.fh)
        logger.addHandler(MyLog.ch)

        logger.debug(msg)
        logger.removeHandler(MyLog.fh)
        logger.removeHandler(MyLog.ch)

    @staticmethod
    def info(msg):
        logger.addHandler(MyLog.fh)
        logger.addHandler(MyLog.ch)

        logger.info(msg)
        logger.removeHandler(MyLog.fh)
        logger.removeHandler(MyLog.ch)

    @staticmethod
    def debug(msg):
        logger.addHandler(MyLog.fh)
        logger.addHandler(MyLog.ch)

        logger.debug(msg)
        logger.removeHandler(MyLog.fh)
        logger.removeHandler(MyLog.ch)

    @staticmethod
    def warning(msg):
        logger.addHandler(MyLog.fh)
        logger.addHandler(MyLog.ch)

        logger.warning(msg)
        logger.removeHandler(MyLog.fh)
        logger.removeHandler(MyLog.ch)

    @staticmethod
    def error(msg):
        logger.addHandler(MyLog.fh)
        logger.addHandler(MyLog.ch)

        logger.error(msg)
        logger.removeHandler(MyLog.fh)
        logger.removeHandler(MyLog.ch)



if __name__ == "__main__":
    MyLog.debug("This is debug message")
    MyLog.info("This is info message")
#     MyLog.warning("This is warning message")
#     MyLog.error("This is error")
#     MyLog.critical("This is critical message")