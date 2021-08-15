#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
    :Author: yuangezhizao
    :Time: 2021/8/15 13:41
    :Site: https://www.yuangezhizao.cn
    :Copyright: © 2021 yuangezhizao <root@yuangezhizao.cn>
"""
import json
import os

import pymongo
import xmltodict

MONGODB_QCLOUD_STRING = 'mongodb://<rm>:<rm>@lab.yuangezhizao.cn:27017/'


def save_to_mongo(music_data):
    music_coll = pymongo.MongoClient(MONGODB_QCLOUD_STRING)['maimai']['music']
    result = music_coll.insert_one(music_data)
    print(result)


def data_converter(music_id, file_path):
    """
    https://www.jianshu.com/p/f7446086516e
    """
    with open(file_path, encoding='utf-8') as f:
        xml_data = f.read()
        _data = xmltodict.parse(xml_data)
        musicdata = json.loads(json.dumps(_data))['MusicData']
        musicdata.pop('@xmlns:xsi')
        musicdata.pop('@xmlns:xsd')
        musicdata['music_id'] = int(music_id)
        print(music_id)
        save_to_mongo(musicdata)


def traverse_folders(params):
    """
    https://www.jianshu.com/p/83991988e45f
    """
    root, dirs, files = params
    for file in files:
        if 'music0' in root and 'xml' in file:
            music_id = root[-6:]
            file_path = os.path.join(root, file)
            data_converter(music_id, file_path)


if __name__ == '__main__':
    root_dirs_files = os.walk('E:\\maimai_Splash\\Package\\Sinmai_Data\\StreamingAssets\\A000\\music')
    while True:
        try:
            traverse_folders(root_dirs_files.__next__())
        except StopIteration:
            break
