#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
    :Author: yuangezhizao-workaccount
    :Time: 2020/10/21 14:40
    :Site: https://www.yuangezhizao.cn
    :Copyright: © 2020 yuangezhizao <root@yuangezhizao.cn>
"""
from maimai_DX_CN_probe import create_app

flask_app = create_app()

if __name__ == '__main__':
    flask_app.run(host='127.0.0.1', port=5000, threaded=True)
