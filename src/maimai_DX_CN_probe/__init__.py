#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
    :Author: yuangezhizao-workaccount
    :Time: 2020/10/21 11:10
    :Site: https://www.yuangezhizao.cn
    :Copyright: © 2020 yuangezhizao <root@yuangezhizao.cn>
"""
import os

import flask
from config import config


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'production')

    app = flask.Flask(__name__, static_url_path='', instance_relative_config=True)

    app.config.from_object(config[config_name])

    register_extensions(app)
    register_blueprints(app)

    return app


def register_extensions(app):
    from maimai_DX_CN_probe.plugins.extensions import db
    db.init_app(app)


def register_blueprints(app):
    from maimai_DX_CN_probe.views import register_views
    register_views(app)
