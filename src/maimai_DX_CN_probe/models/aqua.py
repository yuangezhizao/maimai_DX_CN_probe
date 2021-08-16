#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
    :Author: yuangezhizao
    :Time: 2021/8/16 18:45
    :Site: https://www.yuangezhizao.cn
    :Copyright: © 2021 yuangezhizao <root@yuangezhizao.cn>
"""

from maimai_DX_CN_probe.plugins.extensions import db


class MaiMai2UserMusicDetail(db.Model):
    """
    V31__add_maimai2_table.sql

    CREATE TABLE maimai2_user_music_detail (
        id BIGINT auto_increment PRIMARY KEY,
        music_id       INTEGER,
        level          INTEGER,
        play_count     INTEGER,
        achievement    INTEGER,
        combo_status   INTEGER,
        sync_status    INTEGER,
        deluxscore_max INTEGER,
        score_rank     INTEGER,
        user_id        BIGINT,
        constraint FK8hsx2tb67q8nqxgk
            foreign key (user_id) references maimai2_user_detail (id)
    );
    """
    __bind_key__ = 'aqua'
    __tablename__ = 'maimai2_user_music_detail'

    id = db.Column(db.BIGINT, autoincrement=True, primary_key=True)
    music_id = db.Column(db.Integer)
    level = db.Column(db.Integer)
    play_count = db.Column(db.Integer)
    achievement = db.Column(db.Integer)
    combo_status = db.Column(db.Integer)
    sync_status = db.Column(db.Integer)
    deluxscore_max = db.Column(db.Integer)
    score_rank = db.Column(db.Integer)
    user_id = db.Column(db.BIGINT)

    def __init__(self, music_id, level, play_count, achievement, combo_status, sync_status, deluxscore_max, score_rank,
                 user_id):
        self.music_id = music_id
        self.level = level
        self.play_count = play_count
        self.achievement = achievement
        self.combo_status = combo_status
        self.sync_status = sync_status
        self.deluxscore_max = deluxscore_max
        self.score_rank = score_rank
        self.user_id = user_id

    def __repr__(self):
        return '<MaiMai2UserMusicDetail (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)>' % (
            self.id, self.music_id, self.level, self.play_count, self.achievement, self.combo_status, self.sync_status,
            self.deluxscore_max, self.score_rank, self.user_id)

    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        db.session.commit()
        return self
