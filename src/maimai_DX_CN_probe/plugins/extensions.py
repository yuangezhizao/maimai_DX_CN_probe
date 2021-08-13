#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
    :Author: yuangezhizao
    :Time: 2020/8/1 0001 23:48
    :Site: https://www.yuangezhizao.cn
    :Copyright: © 2019 yuangezhizao <root@yuangezhizao.cn>
"""
from flask_caching import Cache
from flask_compress import Compress
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
compress = Compress()
cache = Cache()
