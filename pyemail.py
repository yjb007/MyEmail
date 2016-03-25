#!/usr/bin/env python
# encoding: utf-8

import os
from MyEmail.MyEmail import myEmail
from MyEmail.utils import getConfig

config_file = 'config.yaml'
config_file = os.path.dirname(os.path.realpath(__file__)) + os.sep + config_file
#os.path.realpath(__file__)查找当前运行脚本的真实路径

if __name__ == '__main__':
    options = getConfig(config_file)
    T = myEmail(options)
    T.sendEmail()

