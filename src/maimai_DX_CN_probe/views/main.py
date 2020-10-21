#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
    :Author: yuangezhizao-workaccount
    :Time: 2020/10/21 11:08
    :Site: https://www.yuangezhizao.cn
    :Copyright: © 2020 yuangezhizao <root@yuangezhizao.cn>
"""
import flask

app = flask.current_app
bp = flask.Blueprint('main', __name__)


@bp.route('/')
def hello_world():
    return 'Hello World!'
