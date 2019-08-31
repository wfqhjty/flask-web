import time


class Utils(object):

    @staticmethod
    def getLocalTime():
        """
        获取当前时间 格式化成2017-01-01 00:00:00形式
        """
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
