#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
    :Author: yuangezhizao-workaccount
    :Time: 2020/10/21 11:10
    :Site: https://www.yuangezhizao.cn
    :Copyright: © 2020 yuangezhizao <root@yuangezhizao.cn>
"""
from flask import Flask


def create_app():
    app = Flask(__name__)

    register_blueprints(app)
    return app


def register_blueprints(app):
    from maimai_DX_CN_probe.views import register_views
    register_views(app)


app = create_app()
