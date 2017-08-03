#!/usr/bin/python
# coding=utf-8
#filename:logger_util.py
#author:Yuncheng Zhu

import logging.handlers

LOG_FILE = "agent.log"

handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes = 1024*1024, backupCount = 5) # 实例化handler
fmt = '%(levelname)s - %(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'

formatter = logging.Formatter(fmt)  # 实例化formatter
handler.setFormatter(formatter)  # 为handler添加formatter

logger = logging.getLogger('agent')
logger.addHandler(handler)  # 为logger添加handler
logger.setLevel(logging.DEBUG)