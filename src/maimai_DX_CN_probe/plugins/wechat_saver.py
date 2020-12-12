#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
    :Author: yuangezhizao
    :Time: 2020/12/12 23:11
    :Site: https://www.yuangezhizao.cn
    :Copyright: © 2020 yuangezhizao <root@yuangezhizao.cn>
"""
import datetime

from lxml import etree

from maimai_DX_CN_probe.models.maimai import HOME, PlayerData, album, Record


def save_home(raw_html):
    selector = etree.HTML(raw_html)

    basic_img = selector.xpath('/html/body/div[2]/div[2]/div[1]/img/@src')[0]
    trophy = selector.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div[1]/div/span/text()')[0]
    name = selector.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/text()')[0]
    rating = selector.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div/text()')[0]
    rating_max = selector.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/text()')[0][4:]
    rating_img = selector.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/img/@src')[0]
    grade_img = selector.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/img[2]/@src')[0]
    star = selector.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div[4]/text()')[0][1:]
    chara = selector.xpath('/html/body/div[2]/div[2]/img/@src')[0]
    comment = selector.xpath('/html/body/div[2]/div[2]/div[2]/text()')[0]
    cache_dt = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

    new_maimai_HOME = HOME(basic_img, trophy, name, rating, rating_max, rating_img, grade_img, star, chara, comment,
                           cache_dt)
    r = new_maimai_HOME.save()
    return r


def save_playerData(raw_html):
    selector = etree.HTML(raw_html)

    music_count = selector.xpath('/html/body/div[2]/div[2]/div[3]/text()')[0].split('：')[1]
    total_count = selector.xpath('/html/body/div[2]/div[2]/div[4]/div[2]/text()')[0].split('/')[1].replace(',', '')

    sssp = selector.xpath('/html/body/div[2]/div[2]/div[4]/div[2]/text()')[0].split('/')[0]
    sss = selector.xpath('/html/body/div[2]/div[2]/div[7]/div[2]/text()')[0].split('/')[0]
    ssp = selector.xpath('/html/body/div[2]/div[2]/div[10]/div[2]/text()')[0].split('/')[0]
    ss = selector.xpath('/html/body/div[2]/div[2]/div[13]/div[2]/text()')[0].split('/')[0]
    sp = selector.xpath('/html/body/div[2]/div[2]/div[16]/div[2]/text()')[0].split('/')[0]
    s = selector.xpath('/html/body/div[2]/div[2]/div[19]/div[2]/text()')[0].split('/')[0]
    clear = selector.xpath('/html/body/div[2]/div[2]/div[22]/div[2]/text()')[0].split('/')[0]

    app = selector.xpath('/html/body/div[2]/div[2]/div[5]/div[2]/text()')[0].split('/')[0]
    ap = selector.xpath('/html/body/div[2]/div[2]/div[8]/div[2]/text()')[0].split('/')[0]
    fcp = selector.xpath('/html/body/div[2]/div[2]/div[11]/div[2]/text()')[0].split('/')[0]
    fc = selector.xpath('/html/body/div[2]/div[2]/div[14]/div[2]/text()')[0].split('/')[0]
    fsdp = selector.xpath('/html/body/div[2]/div[2]/div[17]/div[2]/text()')[0].split('/')[0]
    fsd = selector.xpath('/html/body/div[2]/div[2]/div[20]/div[2]/text()')[0].split('/')[0]
    fsp = selector.xpath('/html/body/div[2]/div[2]/div[23]/div[2]/text()')[0].split('/')[0]
    fs = selector.xpath('/html/body/div[2]/div[2]/div[25]/div[2]/text()')[0].split('/')[0]

    cache_dt = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

    new_maimai_PlayerData = PlayerData(music_count, total_count, sssp, sss, ssp, ss, sp, s, clear, app, ap, fcp, fc,
                                       fsdp, fsd, fsp, fs,
                                       cache_dt)
    r = new_maimai_PlayerData.save()
    return r


def save_playerData_album(raw_html):
    selector = etree.HTML(raw_html)

    new_count = 0
    album_count = len(selector.xpath('.//div[@class=" m_10 p_5 f_0"]'))

    for i in range(album_count + 1, 1, -1):
        dx_img_s = selector.xpath(f'/html/body/div[2]/div[{i}]/div/img[1]/@src')[0].split('/')[-1].split('.')[0]
        play_dt = selector.xpath(f'/html/body/div[2]/div[{i}]/div/div[1]/text()')[0]
        play_dt_utc = datetime.datetime.strptime(play_dt, '%Y/%m/%d %H:%M') - datetime.timedelta(hours=8)
        level_img_s = selector.xpath(f'/html/body/div[2]/div[{i}]/div/img[2]/@src')[0].split('/')[-1].split('.')[0]
        name = selector.xpath(f'/html/body/div[2]/div[{i}]/div/div[3]/text()')[0]
        img = selector.xpath(f'/html/body/div[2]/div[{i}]/div/img[3]/@src')[0].split('/')[-1]
        cache_dt = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        if not album.query.filter(album.play_dt == play_dt).first():
            new_maimai_album = album(dx_img_s, play_dt, play_dt_utc, level_img_s, name, img, cache_dt)
            new_maimai_album.save()
            new_count += 1

    return [new_count, album_count]


def save_record(raw_html):
    selector = etree.HTML(raw_html)

    new_count = 0
    record_count = len(selector.xpath('//div[@class="p_10 t_l f_0 v_b"]'))

    for i in range(record_count + 1, 1, -1):
        level_img_s = selector.xpath(f'/html/body/div[2]/div[{i}]/div[1]/img/@src')[0].split('/')[-1].split('.')[0]
        try:
            vs_img_s = selector.xpath(f'/html/body/div[2]/div[{i}]/div[1]/img[3]/@src')[0] \
                .split('/')[-1].split('.')[0]
        except Exception as e:
            vs_img_s = None

        track = selector.xpath(f'/html/body/div[2]/div[{i}]/div[1]/div[1]/span[1]/text()')[0].split(' ')[1]
        play_dt = selector.xpath(f'/html/body/div[2]/div[{i}]/div[1]/div[1]/span[2]/text()')[0]

        play_dt_utc = datetime.datetime.strptime(play_dt, '%Y/%m/%d %H:%M') - datetime.timedelta(hours=8)
        # play_ts_utc = int(time.mktime(play_dt_utc.timetuple()))

        try:
            selector.xpath(f'/html/body/div[2]/div[{i}]/div[2]/div[1]/img/@src')[0].split('/')[-1].split('.')[0]
            clear = True
        except Exception as e:
            clear = False
        name = selector.xpath(f'/html/body/div[2]/div[{i}]/div[2]/div[1]/text()')[0]
        img_s = selector.xpath(f'/html/body/div[2]/div[{i}]/div[2]/div[2]/img[1]/@src')[0]
        dx_img_s = selector.xpath(f'/html/body/div[2]/div[{i}]/div[2]/div[2]/img[2]/@src')[0] \
            .split('/')[-1].split('.')[0]
        achievement_0 = selector.xpath(f'/html/body/div[2]/div[{i}]/div[2]/div[2]/div/div[2]/text()')[0]
        achievement_1 = selector.xpath(f'/html/body/div[2]/div[{i}]/div[2]/div[2]/div/div[2]/span/text()')[0]
        achievement = int(achievement_0) + float(f'0{achievement_1}'[:-1])
        try:
            selector.xpath(f'/html/body/div[2]/div[{i}]/div[2]/div[2]/div/img[3]/@src')[0]
            score_rank_new = True
            score_rank_img_s = selector.xpath(f'/html/body/div[2]/div[{i}]/div[2]/div[2]/div/img[2]/@src')[0] \
                .split('/')[-1].split('.')[0]
        except Exception as e:
            score_rank_new = False
            score_rank_img_s = selector.xpath(f'/html/body/div[2]/div[{i}]/div[2]/div[2]/div/img[1]/@src')[0] \
                .split('/')[-1].split('.')[0]
        delux_score = selector.xpath(f'/html/body/div[2]/div[{i}]/div[2]/div[2]/div/div[3]/div[1]/div/text()')[0] \
            .split('/')[-1].split('.')[0].replace(',', '')
        try:
            selector.xpath(f'/html/body/div[2]/div[{i}]/div[2]/div[2]/div/div[3]/div[1]/img[2]/@src')[0]
            delux_new = True
        except Exception as e:
            delux_new = False
        fc_img_s = selector.xpath(f'/html/body/div[2]/div[{i}]/div[2]/div[2]/div/div[3]/img[1]/@src')[0] \
            .split('/')[-1].split('.')[0]
        fs_img_s = selector.xpath(f'/html/body/div[2]/div[{i}]/div[2]/div[2]/div/div[3]/img[2]/@src')[0] \
            .split('/')[-1].split('.')[0]
        try:
            rate_img_s = selector.xpath(f'/html/body/div[2]/div[{i}]/div[2]/div[2]/div/div[3]/img[3]/@src')[0] \
                .split('/')[-1].split('.')[0]
        except Exception as e:
            rate_img_s = None
        cache_dt = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

        if not Record.query.filter(Record.play_dt == play_dt).first():
            new_maimai_Record = Record(level_img_s, vs_img_s, track, play_dt, play_dt_utc, clear, name, img_s, dx_img_s,
                                       achievement,
                                       score_rank_new, score_rank_img_s, delux_score, delux_new, fc_img_s, fs_img_s,
                                       rate_img_s, cache_dt)
            new_maimai_Record.save()
            new_count += 1

    return [new_count, record_count]
