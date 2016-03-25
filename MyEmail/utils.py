#!/usr/bin/env python
# encoding: utf-8

import yaml

def getConfig(config_file):
    with open(config_file,'rb') as f:
        config = yaml.load(f)['SMTP']
    return config







