import os
from datetime import datetime
import logging

import coloredlogs
###
# 1. 创建logger实例，如果参数为空则返回root logger
###

logger = logging.getLogger()
# 设置总日志级别, 也可以给不同的handler设置不同的日志级别
#logger.setLevel(logging.DEBUG)
logging_level= logger.setLevel(logging.INFO)


###
# 2. 创建Handler, 输出日志到控制台和文件
###

# 控制台日志和日志文件使用同一个Formatter
#'%(asctime)s - %(filename)s[line:%(lineno)d] - <%(threadName)s %(thread)d> - <Process %(process)d> - %(levelname)s: %(message)s'
formatter = logging.Formatter(
    '%(asctime)s - %(filename)s[line:%(lineno)d]- %(levelname)s: %(message)s'
)

# 日志文件FileHandler

""" 
strabspath=os.path.abspath(__file__)
strdirname=os.path.dirname(strabspath)
str_split=os.path.split(strdirname)
prevdirname=str_split[0]
""" 
def logger_set(str_dirname, opt_verbose= 'OFF'):

    log_dest=os.path.join(str_dirname,"logs") # 日志文件所在目录

    if not os.path.isdir(log_dest):
        os.mkdir(log_dest)
    #filename = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + '.log'  # 日志文件名，以当前时间命名    
    filename = '{0:%Y-%m-%d_%H-%M-%S}.log'.format(datetime.now())
    file_handler = logging.FileHandler(os.path.join(log_dest, filename), encoding='utf-8')  # 创建日志文件handler
    file_handler.setFormatter(formatter)  # 设置Formatter
    # file_handler.setLevel(logging.INFO)  # 单独设置日志文件的日志级别

    # 控制台日志StreamHandler
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    # stream_handler.setLevel(logging.DEBUG)  # 单独设置控制台日志的日志级别

    ###
    # 3. 将handler添加到logger中
    ###

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    #coloredlogs.install(level=logging_level, logger=logger, fmt=formatter)
###
# 或者，使用简单配置
###
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
# logging.debug('This message should appear on the console')

# logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d', level=logging.DEBUG)
# logging.debug('datetime format has changed to 2018-06-01')

# logging.basicConfig(filename='test.log', level=logging.DEBUG)
# logging.debug('This message should go to test.log')
