#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
    :Author: yuangezhizao
    :Time: 2020/1/29 0029 10:50
    :Site: https://www.yuangezhizao.cn
    :Copyright: © 2020 yuangezhizao <root@yuangezhizao.cn>
"""
import re
import time

import requests
from lxml import etree

from maimai_DX_CN_probe.models.maimai import musicInfo_2021

session = requests.Session()


def get_wx_data_musicGenre(cookies):
    genre_dict = {
        101: '流行&动漫',
        102: 'niconico＆VOCALOID',
        103: '东方Project',
        104: '其他游戏',
        105: '舞萌',
        106: '音击/中二节奏',
    }
    diff_dict = {
        0: 'basic',
        1: 'advanced',
        2: 'expert',
        3: 'master',
        4: 'remaster',
    }
    for diff in diff_dict:
        for genre in genre_dict:
            params = f'genre={genre}&diff={diff}'
            print(params)
            url = f'https://maimai.wahlap.com/maimai-mobile/record/musicGenre/search/?{params}'

            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
            }
            if params == 'genre=101&diff=0':
                r = session.get(url, headers=headers, cookies=cookies)
            else:
                # 之后 session 库自行处理 cookies
                r = session.get(url, headers=headers)
            r_text = r.text
            status_code = r.status_code
            if status_code != 200:
                raise Exception('ERROR：status_code != 200')
            if '错误码' in r_text:
                error_code = re.findall('错误码：(.*?)</div>', r_text, re.S)[0]
                raise Exception(f'ERROR：error_code {error_code}')

            music_genre = genre_dict[genre]
            get_music_info(r_text, music_genre)

            time.sleep(1)
            # 防止限频
    print(session.cookies.get_dict())


def update_wx_data_musicWord(cookies):
    word_dict = {
        0: 'あ行',
        1: 'か行',
        2: 'さ行',
        3: 'た行',
        4: 'な行',
        5: 'は行',
        6: 'ま行',
        7: 'や行',
        8: 'ら行',
        9: 'わ行',
        10: 'A～G',
        11: 'H～N',
        12: 'O～U',
        13: 'V～Z',
        14: '数字・その他',
    }
    diff_dict = {
        0: 'basic',
        1: 'advanced',
        2: 'expert',
        3: 'master',
        4: 'remaster',
    }
    for diff in diff_dict:
        for word in word_dict:
            params = f'word={word}&diff={diff}'
            print(params)
            url = f'https://maimai.wahlap.com/maimai-mobile/record/musicWord/search/?{params}'

            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
            }
            if params == 'word=0&diff=0':
                r = session.get(url, headers=headers, cookies=cookies)
            else:
                # 之后 session 库自行处理 cookies
                r = session.get(url, headers=headers)
            r_text = r.text
            status_code = r.status_code
            if status_code != 200:
                raise Exception('ERROR：status_code != 200')
            if '错误码' in r_text:
                error_code = re.findall('错误码：(.*?)</div>', r_text, re.S)[0]
                raise Exception(f'ERROR：error_code {error_code}')

            music_word = word_dict[word]
            update_music_info_musicWord(r_text, music_word)

            time.sleep(1)
            # 防止限频
    print(session.cookies.get_dict())


def update_wx_data_musicVersion(cookies):
    version_dict = {
        0: 'maimai',
        1: 'maimai PLUS',
        2: 'GreeN',
        3: 'GreeN PLUS',
        4: 'ORANGE',
        5: 'ORANGE PLUS',
        6: 'PiNK',
        7: 'PiNK PLUS',
        8: 'MURASAKi',
        9: 'MURASAKi PLUS',
        10: 'MiLK',
        11: 'MiLK PLUS',
        12: 'FiNALE',
        13: '舞萌DX',
        # 14: '其他',  # 暂无铺面
        15: '舞萌DX 2021'
    }
    diff_dict = {
        0: 'basic',
        1: 'advanced',
        2: 'expert',
        3: 'master',
        4: 'remaster',
    }
    for diff in diff_dict:
        for version in version_dict:
            params = f'version={version}&diff={diff}'
            print(params)
            url = f'https://maimai.wahlap.com/maimai-mobile/record/musicVersion/search/?{params}'

            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
            }
            if params == 'version=0&diff=0':
                r = session.get(url, headers=headers, cookies=cookies, verify=0)
            else:
                # 之后 session 库自行处理 cookies
                r = session.get(url, headers=headers)
            r_text = r.text
            status_code = r.status_code
            if status_code != 200:
                raise Exception('ERROR：status_code != 200')
            if '错误码' in r_text:
                error_code = re.findall('错误码：(.*?)</div>', r_text, re.S)[0]
                raise Exception(f'ERROR：error_code {error_code}')

            music_version = version_dict[version]
            music_diff = diff_dict[diff]
            # css 的 class 变了草，需要结合 music_diff
            update_music_info_musicVersion(r_text, music_version, music_diff)

            time.sleep(1)
            # 防止限频
    print(session.cookies.get_dict())


def get_music_info(raw, music_genre):
    selector = etree.HTML(raw)
    record_count = len(selector.xpath('//div[@class="w_450 m_15 p_r f_0"]'))
    for i in range(6, record_count + 6):
        level_img_s = selector.xpath(f'/html/body/div[2]/div[{i}]/div/form/img/@src')[0].split('/')[-1].split('.')[0]
        music_level = selector.xpath(f'/html/body/div[2]/div[{i}]/div/form/div[2]/text()')[0]
        name = selector.xpath(f'/html/body/div[2]/div[{i}]/div/form/div[3]/text()')[0]

        try:
            # dx_img_s_hidden = selector.xpath(f'/html/body/div[2]/div[{i}]/img[1]/@src')[0].split('/')[-1].split('.')[0]
            dx_img_s = selector.xpath(f'/html/body/div[2]/div[{i}]/img[2]/@src')[0].split('/')[-1].split('.')[0]
        except Exception as e:
            dx_img_s = selector.xpath(f'/html/body/div[2]/div[{i}]/img/@src')[0].split('/')[-1].split('.')[0]

        music_word = None
        music_version = None

        ver = 'Ver.CH1.11-B'
        new_maimai_Record = musicInfo_2021(name, level_img_s, dx_img_s, music_genre, music_word, music_level,
                                           music_version, ver)
        r = new_maimai_Record.save()
        print(r)


def update_music_info_musicWord(raw, music_word):
    flag = False
    selector = etree.HTML(raw)
    record_count = len(selector.xpath('//div[@class="w_450 m_15 p_r f_0"]'))
    for i in range(6, record_count + 6):
        level_img_s = selector.xpath(f'/html/body/div[2]/div[{i}]/div/form/img/@src')[0].split('/')[-1].split('.')[0]
        music_level = selector.xpath(f'/html/body/div[2]/div[{i}]/div/form/div[2]/text()')[0]
        name = selector.xpath(f'/html/body/div[2]/div[{i}]/div/form/div[3]/text()')[0]

        try:
            # dx_img_s_hidden = selector.xpath(f'/html/body/div[2]/div[{i}]/img[1]/@src')[0].split('/')[-1].split('.')[0]
            dx_img_s = selector.xpath(f'/html/body/div[2]/div[{i}]/img[2]/@src')[0].split('/')[-1].split('.')[0]
        except Exception as e:
            dx_img_s = selector.xpath(f'/html/body/div[2]/div[{i}]/img/@src')[0].split('/')[-1].split('.')[0]

        if (name == 'Link') & (level_img_s == 'diff_advanced'):
            if not flag:
                flag = True
                old_maimai_Record = musicInfo_2021.query.filter_by(name=name, level_img_s=level_img_s,
                                                                   dx_img_s=dx_img_s,
                                                                   music_level=music_level).first()
            else:
                old_maimai_Record = \
                    musicInfo_2021.query.filter_by(name=name, level_img_s=level_img_s, dx_img_s=dx_img_s,
                                                   music_level=music_level).all()[1]
        # Bug need fixed
        else:
            old_maimai_Record = musicInfo_2021.query.filter_by(name=name, level_img_s=level_img_s, dx_img_s=dx_img_s,
                                                               music_level=music_level).first()
        if old_maimai_Record is not None:
            old_maimai_Record.music_word = music_word
            r = old_maimai_Record.update()
            print(r)
        else:
            raise Exception('404')


def update_music_info_musicVersion(raw, music_version, music_diff):
    flag = False
    selector = etree.HTML(raw)
    record_count = len(selector.xpath(f'//div[@class="music_{music_diff}_score_back pointer w_450 m_15 p_3 f_0"]'))
    for i in range(6, record_count + 6):
        level_img_s = selector.xpath(f'/html/body/div[2]/div[{i}]/form/img[1]/@src')[0].split('/')[-1].split('.')[0]
        # 容错，少了一个 div
        music_level = selector.xpath(f'/html/body/div[2]/div[{i}]/form/div[2]/text()')[0]
        # 容错 +1
        name = selector.xpath(f'/html/body/div[2]/div[{i}]/form/div[3]/text()')[0]
        # 容错 +1

        if music_version in ['舞萌DX', '舞萌DX 2021']:
            # DX only
            dx_img_s = 'music_dx'
        else:
            dx_img_s = 'music_standard'

        if (name == 'Link') & (level_img_s == 'diff_advanced'):
            if not flag:
                flag = True
                old_maimai_Record = musicInfo_2021.query.filter_by(name=name, level_img_s=level_img_s,
                                                                   dx_img_s=dx_img_s,
                                                                   music_level=music_level).first()
            else:
                old_maimai_Record = \
                    musicInfo_2021.query.filter_by(name=name, level_img_s=level_img_s, dx_img_s=dx_img_s,
                                                   music_level=music_level).all()[1]
        # Bug need fixed
        else:
            old_maimai_Record = musicInfo_2021.query.filter_by(name=name, level_img_s=level_img_s, dx_img_s=dx_img_s,
                                                               music_level=music_level).first()
        if old_maimai_Record is not None:
            old_maimai_Record.music_version = music_version
            r = old_maimai_Record.update()
            print(r)
        else:
            raise Exception('404')
