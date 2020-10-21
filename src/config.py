#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
    :Author: yuangezhizao-workaccount
    :Time: 2020/10/21 15:37
    :Site: https://www.yuangezhizao.cn
    :Copyright: © 2020 yuangezhizao <root@yuangezhizao.cn>
"""
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestingConfig(BaseConfig):
    TESTING = True


class ProductionConfig(BaseConfig):
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': ProductionConfig
}
