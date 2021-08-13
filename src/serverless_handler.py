#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
    :Author: yuangezhizao-workaccount
    :Time: 2020/10/21 11:15
    :Site: https://www.yuangezhizao.cn
    :Copyright: © 2020 yuangezhizao <root@yuangezhizao.cn>
"""
import sl_wsgi
from maimai_DX_CN_probe import create_app  # Replace with your actual application


# If you need to send additional content types as text, add then directly
# to the whitelist:
#
# sl_wsgi.TEXT_MIME_TYPES.append("application/custom+json")

def handler(event, context):
    return sl_wsgi.handle_request(create_app(), event, context)
