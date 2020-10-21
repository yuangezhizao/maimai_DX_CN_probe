#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
    :Author: yuangezhizao-workaccount
    :Time: 2020/10/21 11:08
    :Site: https://www.yuangezhizao.cn
    :Copyright: © 2020 yuangezhizao <root@yuangezhizao.cn>
"""
import flask

from maimai_DX_CN_probe.models.maimai import HOME

app = flask.current_app
bp = flask.Blueprint('main', __name__)


@bp.route('/')
def site_index():
    return flask.render_template('index.html')


@bp.route('/wechat_archive')
def wechat_archive():
    if 'home' in flask.request.args:
        HOME_data = HOME.query.order_by(HOME.id.desc()).all()

        id_data, rating_data, rating_max_data, star_data, cache_dt_data = [], [], [], [], []
        for data in HOME_data:
            id_data.append(data.id)
            rating_data.append(data.rating / 100)
            rating_max_data.append(data.rating_max / 100)
            star_data.append(data.star)
            cache_dt_data.append(data.cache_dt.strftime('%Y-%m-%d %H:%M:%S'))

        return flask.render_template('maimai/home.html', HOME_data=HOME_data, id_data=id_data, rating_data=rating_data,
                                     rating_max_data=rating_max_data, star_data=star_data, cache_dt_data=cache_dt_data)
    else:
        return flask.redirect(flask.url_for('main.wechat_archive', _external=True) + '?home')
