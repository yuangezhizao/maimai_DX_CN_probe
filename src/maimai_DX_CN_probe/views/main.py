#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
    :Author: yuangezhizao-workaccount
    :Time: 2020/10/21 11:08
    :Site: https://www.yuangezhizao.cn
    :Copyright: © 2020 yuangezhizao <root@yuangezhizao.cn>
"""
import flask

from maimai_DX_CN_probe.models.maimai import HOME, PlayerData, album, Record, playlogDetail, musicInfo, \
    practice
from maimai_DX_CN_probe.plugins.wechat_saver import save_home, save_playerData, save_playerData_album, save_record, \
    save_record_playlogDetail

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

        return flask.render_template('maimai/wechat_archive/home.html', HOME_data=HOME_data, id_data=id_data,
                                     rating_data=rating_data,
                                     rating_max_data=rating_max_data, star_data=star_data, cache_dt_data=cache_dt_data)
    elif 'playerData' in flask.request.args:
        playerData = PlayerData.query.order_by(PlayerData.id.desc()).all()

        id_data, music_count_data, total_count_data, sssp_data, sss_data, ssp_data, ss_data, sp_data, s_data, clear_data = [], [], [], [], [], [], [], [], [], []
        app_data, ap_data, fcp_data, fc_data, fsdp_data, fsd_data, fsp_data, fs_data, cache_dt_data = [], [], [], [], [], [], [], [], []

        for data in playerData:
            id_data.append(data.id)
            music_count_data.append(data.music_count)
            total_count_data.append(data.total_count)

            sssp_data.append(data.sssp)
            sss_data.append(data.sss)
            ssp_data.append(data.ssp)
            ss_data.append(data.ss)
            sp_data.append(data.sp)
            s_data.append(data.s)
            clear_data.append(data.clear)

            app_data.append(data.app)
            ap_data.append(data.ap)
            fcp_data.append(data.fcp)
            fc_data.append(data.fc)
            fsdp_data.append(data.fsdp)
            fsd_data.append(data.fsd)
            fsp_data.append(data.fsp)
            fs_data.append(data.fs)
            cache_dt_data.append(data.cache_dt.strftime('%Y-%m-%d %H:%M:%S'))

        return flask.render_template('maimai/wechat_archive/playerData.html', playerData=playerData, id_data=id_data,
                                     music_count_data=music_count_data, total_count_data=total_count_data,
                                     sssp_data=sssp_data, sss_data=sss_data, ssp_data=ssp_data, ss_data=ss_data,
                                     sp_data=sp_data, s_data=s_data, clear_data=clear_data, app_data=app_data,
                                     ap_data=ap_data, fcp_data=fcp_data, fc_data=fc_data, fsdp_data=fsdp_data,
                                     fsd_data=fsd_data, fsp_data=fsp_data, fs_data=fs_data, cache_dt_data=cache_dt_data)
    elif 'playerData_album' in flask.request.args:
        playerData_album = album.query.order_by(album.id.desc()).all()
        return flask.render_template('maimai/wechat_archive/playerData_album.html', playerData_album=playerData_album)
    elif 'record' in flask.request.args:
        record_data = Record.query.order_by(Record.id.desc()).all()
        return flask.render_template('maimai/wechat_archive/record.html', record_data=record_data)
    elif 'record_playlogDetail' in flask.request.args:
        idx = int(flask.request.args.get('idx'))
        all_levels = flask.request.args.get('all_levels')
        id = idx - 1

        # 基础查询
        record_data = Record.query.get_or_404(idx)
        record_playlogDetail = playlogDetail.query.get(id)

        # 历史 record 查询
        if all_levels == '1':
            record_data_history_all = Record.query.filter_by(name=record_data.name).order_by(
                Record.id.desc()).all()
        else:
            record_data_history_all = Record.query.filter_by(name=record_data.name,
                                                             level_img_s=record_data.level_img_s).order_by(
                Record.id.desc()).all()

        # 历史 record id 提取
        id_all, record_playlogDetail_history_all = [], []
        achievement_data, delux_score_data, fc_img_s_data, fs_img_s_data, cache_dt_data = [], [], [], [], []

        for record_data_history in record_data_history_all:
            id_all.append(record_data_history.id - 1)
            achievement_data.append(record_data_history.achievement)
            delux_score_data.append(record_data_history.delux_score)
            fc_img_s_data.append(100 if record_data_history.fc_img_s != 'fc_dummy' else 99)
            fs_img_s_data.append(100 if record_data_history.fs_img_s != 'fs_dummy' else 99)
            cache_dt_data.append(record_data_history.cache_dt.strftime('%Y-%m-%d %H:%M:%S'))

        # 历史 record_playlogDetail 查询
        for id in id_all:
            record_playlogDetail_history = playlogDetail.query.filter_by(id=id).all()[0]
            record_playlogDetail_history_all.append(record_playlogDetail_history)

        return flask.render_template('maimai/wechat_archive/record_playlogDetail.html', record_data=record_data,
                                     count=len(id_all), record_playlogDetail=record_playlogDetail,
                                     record_data_history_all=record_data_history_all,
                                     record_playlogDetail_history_all=record_playlogDetail_history_all,
                                     achievement_data=achievement_data, delux_score_data=delux_score_data,
                                     fc_img_s_data=fc_img_s_data, fs_img_s_data=fs_img_s_data,
                                     cache_dt_data=cache_dt_data, all_levels=all_levels)
    else:
        return flask.redirect(flask.url_for('main.wechat_archive', _external=True) + '?home')


@bp.route('/wechat_saver', methods=['GET', 'POST'])
def wechat_saver():
    auto_saver = flask.request.args.get('auto_saver')
    if auto_saver:
        if flask.request.method == 'POST':
            func_type = flask.request.form.get('func_type')
            userId = flask.request.form.get('userId')
            _t = flask.request.form.get('_t')
            if func_type == 'record_playlogDetail':
                start_posi = int(flask.request.form.get('start_posi'))
                end_posi = int(flask.request.form.get('end_posi'))
                r = save_record_playlogDetail(userId, _t, start_posi, end_posi)
                if 'ERROR' not in r:
                    flask.flash(f'[详细] 存储成功：{r}', 'success')
                else:
                    flask.flash(f'[详细] 存储失败：{r}', 'negative')
            else:
                flask.flash(f'非法 [func_type]', 'negative')
        return flask.render_template('maimai/wechat_saver/auto.html')
    else:
        if flask.request.method == 'POST':
            html_type = flask.request.form.get('html_type')
            raw_html = flask.request.form.get('raw_html')
            if html_type == 'home':
                r = save_home(raw_html)
                flask.flash(f'[主页] 存储成功：{r}', 'success')
            elif html_type == 'playerData':
                r = save_playerData(raw_html)
                flask.flash(f'[游戏数据] 存储成功：{r}', 'success')
            elif html_type == 'playerData_album':
                r = save_playerData_album(raw_html)
                flask.flash(f'[相册] 存储成功：{r}', 'success')
            elif html_type == 'record':
                r = save_record(raw_html)
                flask.flash(f'[游戏记录] 存储成功：{r}', 'success')
            else:
                flask.flash(f'非法 [html_type]', 'negative')
        return flask.render_template('maimai/wechat_saver/manual.html')


@bp.route('/record')
def record():
    if 'practice' in flask.request.args:
        practice_data = practice.query.order_by(practice.id.asc()).all()
        return flask.render_template('maimai/review/practice.html', practice_data=practice_data)
    else:
        page = int(flask.request.args.get('page', 1))
        per_page = int(flask.request.args.get('per_page', 20))
        if 'all' in flask.request.args:
            per_page = 334
        if 'diff' in flask.request.args:
            record_data_paginate = Record.query.order_by(Record.id.desc()).paginate(page, per_page)
            history_record_data = []
            record_playlogDetail_data = []
            for record_data in record_data_paginate.items:
                _id = record_data.id
                _record_playlogDetail = playlogDetail.query.get(_id - 1)

                record_playlogDetail_data.append(_record_playlogDetail)

                _level_img_s = record_data.level_img_s
                _name = record_data.name
                _play_dt = record_data.play_dt
                _dx_img_s = record_data.dx_img_s
                _record_data = Record.query.filter_by(name=_name, level_img_s=_level_img_s, dx_img_s=_dx_img_s).filter(
                    Record.play_dt <= _play_dt).order_by(
                    Record.achievement.desc()).all()

                history_record_data.append(_record_data)

            return flask.render_template('maimai/record/diff.html',
                                         record_data_paginate=record_data_paginate,
                                         record_playlogDetail_data=record_playlogDetail_data,
                                         history_record_data=history_record_data, page=page, per_page=per_page)
        else:
            record_data_paginate = Record.query.order_by(Record.id.desc()).paginate(page, per_page)
            # total = record_data_paginate.total
            # total_page = math.ceil(total / per_page)
            return flask.render_template('maimai/record/index.html', record_data_paginate=record_data_paginate,
                                         page=page, per_page=per_page)


@bp.route('/info', methods=['GET', 'POST'])
def info():
    record_musicGenre_data = []
    if flask.request.method == 'POST':
        filters = []
        name = flask.request.form.get('name')
        if name:
            filters.append(musicInfo.name.like('%' + name + '%'))
        level_img_s = flask.request.form.get('level_img_s')
        if level_img_s:
            filters.append(musicInfo.level_img_s == level_img_s)
        dx_img_s = flask.request.form.get('dx_img_s')
        if dx_img_s:
            filters.append(musicInfo.dx_img_s == dx_img_s)

        music_genre = flask.request.form.get('music_genre')
        if music_genre:
            filters.append(musicInfo.music_genre == music_genre)
        music_word = flask.request.form.get('music_word')
        if music_word:
            filters.append(musicInfo.music_word == music_word)
        music_level = flask.request.form.get('music_level')
        if music_level:
            filters.append(musicInfo.music_level == music_level)
        music_version = flask.request.form.get('music_version')
        if music_version:
            filters.append(musicInfo.music_version == music_version)

        ver = flask.request.form.get('ver')
        if ver:
            filters.append(musicInfo.ver == ver)
        flask.flash(f'筛选：{filters}', 'success')

        record_musicGenre_data = musicInfo.query.filter(*filters).order_by(musicInfo.id.asc()).all()
    return flask.render_template('maimai/info/list.html', record_musicGenre_data=record_musicGenre_data,
                                 size=len(record_musicGenre_data))


@bp.route('/rating')
def rating():
    coefficient_dict = {
        'sssplus': 15,
        'sss': 14,
        'ssplus': 13,
        'ss': 12,
        'splus': 11,
        's': 10,
        'aaa': 9.4,
    }
    if 'calc' in flask.request.args:
        music_record_data = Record.query.filter_by(single_rating=0).all()

        for music_record in music_record_data:
            if music_record.name == 'FREEDOM DiVE (tpz Overcute Remix)':
                continue
            _music_info = musicInfo.query.filter_by(name=music_record.name,
                                                    level_img_s=music_record.level_img_s,
                                                    dx_img_s=music_record.dx_img_s).first()
            print(_music_info)

            # TODO：曲名有重复
            _constant = _music_info.constant  # 定数
            _music_level = _music_info.music_level  # 等级
            try:
                _coefficient = coefficient_dict[music_record.score_rank_img_s]  # 系数
            except Exception as e:
                _coefficient = -1

            _achievement = music_record.achievement / 100 if music_record.achievement / 100 <= 1.005 else 1.005  # 上限 100.5%
            music_record._achievement = _achievement

            _single_rating = _constant * _coefficient * _achievement  # 单曲 RATING

            music_record.single_rating = _single_rating
            music_record.update()

        return '单曲 RATING 计算存储完成'
    single_rating_calc = 0
    music_dx_standard_record_data = []
    music_dx_record_data = Record.query.filter_by(dx_img_s='music_dx').order_by(Record.single_rating.desc()).limit(15)
    music_standard_record_data = Record.query.filter_by(dx_img_s='music_standard').order_by(
        Record.single_rating.desc()).limit(25)
    for music_dx_record in music_dx_record_data:
        _music_dx_info = musicInfo.query.filter_by(name=music_dx_record.name, level_img_s=music_dx_record.level_img_s,
                                                   dx_img_s='music_dx').first()
        # TODO：曲名有重复
        _constant = _music_dx_info.constant  # 定数
        music_dx_record.constant = _constant
        _music_level = _music_dx_info.music_level  # 等级
        music_dx_record.music_level = _music_level
        _coefficient = coefficient_dict[music_dx_record.score_rank_img_s]  # 系数
        music_dx_record.coefficient = _coefficient

        _achievement = music_dx_record.achievement / 100 if music_dx_record.achievement / 100 <= 1.005 else 1.005  # 上限 100.5%
        music_dx_record._achievement = _achievement

        single_rating_calc = single_rating_calc + int(music_dx_record.single_rating)  # 单曲 RATING 累加
        music_dx_standard_record_data.append(music_dx_record)
    for music_standard_record in music_standard_record_data:
        _music_standard_info = musicInfo.query.filter_by(name=music_standard_record.name,
                                                         level_img_s=music_standard_record.level_img_s,
                                                         dx_img_s='music_standard').first()
        # TODO：曲名有重复
        _constant = _music_standard_info.constant  # 定数
        music_standard_record.constant = _constant
        _music_level = _music_standard_info.music_level  # 等级
        music_standard_record.music_level = _music_level
        _coefficient = coefficient_dict[music_standard_record.score_rank_img_s]  # 系数
        music_standard_record.coefficient = _coefficient

        _achievement = music_standard_record.achievement / 100 if music_standard_record.achievement / 100 <= 1.005 else 1.005  # 上限 100.5%
        music_standard_record._achievement = _achievement

        single_rating_calc = single_rating_calc + int(music_standard_record.single_rating)  # 单曲 RATING 累加
        music_dx_standard_record_data.append(music_standard_record)
    return flask.render_template('maimai/rating/calc.html', music_dx_standard_record_data=music_dx_standard_record_data,
                                 single_rating_calc=single_rating_calc)
