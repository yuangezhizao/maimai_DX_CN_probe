#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
    :Author: nyaadevs & yuangezhizao-workaccount
    :Time: 2020/10/21 11:09
    :Site: https://www.yuangezhizao.cn
    :Copyright: © 2020 yuangezhizao <root@yuangezhizao.cn>
"""


def register_views(flask_app):
    """ Register the blueprints using the flask_app object """
    from maimai_DX_CN_probe.views import (
        main,
    )
    flask_app.register_blueprint(main.bp)
