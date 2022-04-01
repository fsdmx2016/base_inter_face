import logging
import os
import datetime

rootPath = os.path.abspath(os.path.split(os.path.abspath(os.path.realpath(__file__)))[0] + "/../" + "/result/log") + "/"


class Logger(object):
    def __init__(self, logger_name='logs…'):
        self.logger = logging.getLogger(logger_name)
        logging.root.setLevel(logging.NOTSET)
        self.log_file_name = 'log_' + str(datetime.date.today()) + '.txt'  # 日志文件的名称
        self.backup_count = 7  # 最多存放日志的数量
        # 日志输出级别
        self.console_output_level = 'INFO'
        self.file_output_level = 'DEBUG'
        # 日志输出格式
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def get_logger(self):
        """在logger中添加日志句柄并返回，如果logger已有句柄，则直接返回"""
        if not self.logger.handlers:  # 避免重复日志
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)
            # # 每天重新创建一个日志文件，最多保留backup_count份
            # file_handler = TimedRotatingFileHandler(filename=os.path.join(rootPath, self.log_file_name), when='D',
            #                                         interval=1, backupCount=self.backup_count, delay=True,
            #                                         encoding='utf-8')
            # file_handler.setFormatter(self.formatter)
            # file_handler.setLevel(self.file_output_level)
            # self.logger.addHandler(file_handler)
        return self.logger


# 清理上个月的日志
def clean_log():
    # 设置日志存放路径
    if not os.path.exists(rootPath):
        os.mkdir(rootPath)
    # 获取今天的日期 格式 年 月 日
    today_date = str(datetime.date.today())
    # # 定义日志
    # logging.basicConfig(filename=rootPath + 'log_' + today_date + '.txt', level=logging.DEBUG, filemode='a',
    #                     format='【%(asctime)s】 【%(levelname)s】 >>>  %(message)s', datefmt='%Y-%m-%d %H:%M')
    # 遍历目录下的所有日志文件 i是文件名
    filePath = os.path.abspath(os.path.split(os.path.abspath(os.path.realpath(__file__)))[0] + "/../" + "/result/log")
    if os.listdir(filePath):
        for i in os.listdir(rootPath):
            file_path = rootPath + i  # 生成日志文件的路径
            # 获取日志的年月，和今天的年月
            today_m = int(today_date[5:7])  # 今天的月份
            m = int(i[9:11])  # 日志的月份
            today_y = int(today_date[0:4])  # 今天的年份
            y = int(i[4:8])  # 日志的年份
            # 对上个月的日志进行清理，即删除。
            if m < today_m:
                if os.path.exists(file_path):  # 判断生成的路径对不对，防止报错
                    os.remove(file_path)  # 删除文件
            elif y < today_y:
                if os.path.exists(file_path):
                    os.remove(file_path)
            print("无需清理日志")
    else:
        print("log目录下无日志文件，无需清理日志")


logger = Logger().get_logger()

if __name__ == '__main__':
    clean_log()
    # logger.info("测试")
