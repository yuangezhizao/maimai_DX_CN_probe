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


class ReverseProxied(object):
    # Flask url_for generating http URL instead of https
    # https://stackoverflow.com/questions/14810795/flask-url-for-generating-http-url-instead-of-https

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        environ['wsgi.url_scheme'] = 'https'
        return self.app(environ, start_response)


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'production')

    app = flask.Flask(__name__, static_url_path='', instance_relative_config=True)
    if config_name == 'production':
        app.wsgi_app = ReverseProxied(app.wsgi_app)

    app.config.from_object(config[config_name])
    app.config.from_pyfile(f'{config_name}.py')

    register_extensions(app)
    register_blueprints(app)

    return app


def register_extensions(app):
    from maimai_DX_CN_probe.plugins.extensions import db
    db.init_app(app)


def register_blueprints(app):
    from maimai_DX_CN_probe.views import register_views
    register_views(app)
