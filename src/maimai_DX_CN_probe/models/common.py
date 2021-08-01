#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
    :Author: yuangezhizao
    :Time: 2021/7/28 20:49
    :Site: https://www.yuangezhizao.cn
    :Copyright: © 2021 yuangezhizao <root@yuangezhizao.cn>
"""
from maimai_DX_CN_probe.plugins.extensions import db


class HasId(object):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)


class HasTime(object):
    create_time = db.Column(db.TIMESTAMP, nullable=False, server_default=db.text('CURRENT_TIMESTAMP'))
    update_time = db.Column(db.TIMESTAMP, nullable=False,
                            server_default=db.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
