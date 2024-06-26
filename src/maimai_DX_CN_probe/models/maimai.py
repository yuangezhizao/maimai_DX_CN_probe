#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
    :Author: yuangezhizao
    :Time: 2020/1/29 0029 10:49
    :Site: https://www.yuangezhizao.cn
    :Copyright: © 2020 yuangezhizao <root@yuangezhizao.cn>
"""
from maimai_DX_CN_probe.models.common import HasId, HasTime
from maimai_DX_CN_probe.plugins.extensions import db


class HOME(db.Model, HasId, HasTime):
    __bind_key__ = 'maimai'
    __tablename__ = 'home'

    basic_img = db.Column(db.VARCHAR(255))
    trophy = db.Column(db.VARCHAR(50))
    name = db.Column(db.VARCHAR(50))
    rating = db.Column(db.Integer)
    rating_max = db.Column(db.Integer)
    rating_img = db.Column(db.VARCHAR(255))
    grade_img = db.Column(db.VARCHAR(255))
    star = db.Column(db.Integer)
    chara = db.Column(db.VARCHAR(255))
    comment = db.Column(db.VARCHAR(255))

    def __init__(self, basic_img, trophy, name, rating, rating_max, rating_img, grade_img, star, chara, comment):
        self.basic_img = basic_img,
        self.trophy = trophy,
        self.name = name,
        self.rating = rating,
        self.rating_max = rating_max,
        self.rating_img = rating_img,
        self.grade_img = grade_img,
        self.star = star,
        self.chara = chara,
        self.comment = comment

    def __repr__(self):
        return '<HOME (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)>' % (
            self.id, self.basic_img, self.trophy, self.name, self.rating, self.rating_max, self.rating_img,
            self.grade_img, self.star, self.chara, self.comment
        )

    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        db.session.commit()
        return self


class PlayerData(db.Model, HasId, HasTime):
    __bind_key__ = 'maimai'
    __tablename__ = 'playerdata'

    music_count = db.Column(db.Integer)
    total_count = db.Column(db.Integer)

    sssp = db.Column(db.Integer)
    sss = db.Column(db.Integer)
    ssp = db.Column(db.Integer)
    ss = db.Column(db.Integer)
    sp = db.Column(db.Integer)
    s = db.Column(db.Integer)
    clear = db.Column(db.Integer)

    app = db.Column(db.Integer)
    ap = db.Column(db.Integer)
    fcp = db.Column(db.Integer)
    fc = db.Column(db.Integer)
    fsdp = db.Column(db.Integer)
    fsd = db.Column(db.Integer)
    fsp = db.Column(db.Integer)
    fs = db.Column(db.Integer)

    def __init__(self, music_count, total_count, sssp, sss, ssp, ss, sp, s, clear, app, ap, fcp, fc, fsdp, fsd, fsp,
                 fs):
        self.music_count = music_count,
        self.total_count = total_count,

        self.sssp = sssp,
        self.sss = sss,
        self.ssp = ssp,
        self.ss = ss,
        self.sp = sp,
        self.s = s,
        self.clear = clear,

        self.app = app,
        self.ap = ap,
        self.fcp = fcp,
        self.fc = fc,
        self.fsdp = fsdp,
        self.fsd = fsd,
        self.fsp = fsp,
        self.fs = fs

    def __repr__(self):
        return '<PlayerData (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)>' % (
            self.id, self.music_count, self.total_count, self.sssp, self.sss, self.ssp, self.ss, self.sp, self.s,
            self.clear, self.app, self.ap, self.fcp, self.fc, self.fsdp, self.fsd, self.fsp, self.fs
        )

    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        db.session.commit()
        return self


class album(db.Model, HasId, HasTime):
    __bind_key__ = 'maimai'
    __tablename__ = 'album'

    id = db.Column(db.Integer, primary_key=True)

    dx_img_s = db.Column(db.VARCHAR(50))
    play_dt = db.Column(db.DateTime, nullable=False)
    level_img_s = db.Column(db.VARCHAR(50))
    name = db.Column(db.VARCHAR(50))
    img = db.Column(db.VARCHAR(50), nullable=False)

    def __init__(self, dx_img_s, play_dt, level_img_s, name, img):
        self.dx_img_s = dx_img_s,
        self.play_dt = play_dt,
        self.level_img_s = level_img_s,
        self.name = name,
        self.img = img

    def __repr__(self):
        return '<album (%s, %s, %s, %s, %s, %s)>' % (
            self.id, self.dx_img_s, self.play_dt, self.level_img_s, self.name, self.img
        )

    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        db.session.commit()
        return self


class Record(db.Model, HasId, HasTime):
    __bind_key__ = 'maimai'
    __tablename__ = 'record'

    level_img_s = db.Column(db.VARCHAR(50))
    vs_img_s = db.Column(db.VARCHAR(50))
    track = db.Column(db.Integer)
    play_dt = db.Column(db.DateTime, nullable=False)

    clear = db.Column(db.Boolean)
    name = db.Column(db.VARCHAR(50))
    img_s = db.Column(db.VARCHAR(255))
    dx_img_s = db.Column(db.VARCHAR(50))
    achievement = db.Column(db.Float(4))
    score_rank_new = db.Column(db.Boolean)
    score_rank_img_s = db.Column(db.VARCHAR(50))
    delux_score = db.Column(db.Integer)
    delux_new = db.Column(db.Boolean)

    fc_img_s = db.Column(db.VARCHAR(50))
    fs_img_s = db.Column(db.VARCHAR(50))
    rate_img_s = db.Column(db.VARCHAR(50))

    single_rating = db.Column(db.FLOAT(4), default=0)

    def __init__(self, level_img_s, vs_img_s, track, play_dt, clear, name, img_s, dx_img_s, achievement, score_rank_new,
                 score_rank_img_s, delux_score, delux_new, fc_img_s, fs_img_s, rate_img_s):
        self.level_img_s = level_img_s,
        self.vs_img_s = vs_img_s,
        self.track = track,
        self.play_dt = play_dt,
        self.clear = clear
        self.name = name,
        self.img_s = img_s,
        self.dx_img_s = dx_img_s,
        self.achievement = achievement,
        self.score_rank_new = score_rank_new
        self.score_rank_img_s = score_rank_img_s,
        self.delux_score = delux_score,
        self.delux_new = delux_new
        self.fc_img_s = fc_img_s,
        self.fs_img_s = fs_img_s,
        self.rate_img_s = rate_img_s

    def __repr__(self):
        return '<PlayerData (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)>' % (
            self.level_img_s, self.vs_img_s, self.track, self.play_dt, self.clear, self.name, self.img_s, self.dx_img_s,
            self.achievement, self.score_rank_new, self.score_rank_img_s, self.delux_score, self.delux_new,
            self.fc_img_s, self.fs_img_s, self.rate_img_s, self.single_rating
        )

    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        db.session.commit()
        return self


class playlogDetail(db.Model):
    __bind_key__ = 'maimai'
    __tablename__ = 'playlogdetail'

    id = db.Column(db.Integer, primary_key=True)

    vs_rank = db.Column(db.VARCHAR(50))
    vs_achievement = db.Column(db.Float(4))
    vs_rating = db.Column(db.Integer)
    vs_grade = db.Column(db.VARCHAR(50))

    chara_0_img_s = db.Column(db.VARCHAR(50))
    chara_0_star = db.Column(db.Integer)
    chara_0_lv = db.Column(db.Integer)
    chara_1_img_s = db.Column(db.VARCHAR(50))
    chara_1_star = db.Column(db.Integer)
    chara_1_lv = db.Column(db.Integer)
    chara_2_img_s = db.Column(db.VARCHAR(50))
    chara_2_star = db.Column(db.Integer)
    chara_2_lv = db.Column(db.Integer)
    chara_3_img_s = db.Column(db.VARCHAR(50))
    chara_3_star = db.Column(db.Integer)
    chara_3_lv = db.Column(db.Integer)
    chara_4_img_s = db.Column(db.VARCHAR(50))
    chara_4_star = db.Column(db.Integer)
    chara_4_lv = db.Column(db.Integer)

    fast = db.Column(db.Integer)
    late = db.Column(db.Integer)
    grade = db.Column(db.Integer)
    grade_diff = db.Column(db.VARCHAR(50))
    rating = db.Column(db.Integer)
    delux_rating = db.Column(db.Integer)

    delux_rating_diff = db.Column(db.VARCHAR(50))
    grade_pic_s = db.Column(db.VARCHAR(50))

    notes_tap_cp = db.Column(db.Integer)
    notes_tap_p = db.Column(db.Integer)
    notes_tap_great = db.Column(db.Integer)
    notes_tap_good = db.Column(db.Integer)
    notes_tap_miss = db.Column(db.Integer)

    notes_hold_cp = db.Column(db.Integer)
    notes_hold_p = db.Column(db.Integer)
    notes_hold_great = db.Column(db.Integer)
    notes_hold_good = db.Column(db.Integer)
    notes_hold_miss = db.Column(db.Integer)

    notes_slide_cp = db.Column(db.Integer)
    notes_slide_p = db.Column(db.Integer)
    notes_slide_great = db.Column(db.Integer)
    notes_slide_good = db.Column(db.Integer)
    notes_slide_miss = db.Column(db.Integer)

    notes_touch_cp = db.Column(db.Integer)
    notes_touch_p = db.Column(db.Integer)
    notes_touch_great = db.Column(db.Integer)
    notes_touch_good = db.Column(db.Integer)
    notes_touch_miss = db.Column(db.Integer)

    notes_break_cp = db.Column(db.Integer)
    notes_break_p = db.Column(db.Integer)
    notes_break_great = db.Column(db.Integer)
    notes_break_good = db.Column(db.Integer)
    notes_break_miss = db.Column(db.Integer)

    maxcombo = db.Column(db.VARCHAR(50))
    maxsync = db.Column(db.VARCHAR(50))
    level_img_s = db.Column(db.VARCHAR(50))
    name = db.Column(db.VARCHAR(50))

    cache_dt = db.Column(db.DateTime, nullable=False)

    def __init__(self, vs_rank, vs_achievement, vs_rating, vs_grade, chara_0_img_s, chara_0_star, chara_0_lv,
                 chara_1_img_s, chara_1_star, chara_1_lv, chara_2_img_s,
                 chara_2_star, chara_2_lv, chara_3_img_s, chara_3_star, chara_3_lv, chara_4_img_s, chara_4_star,
                 chara_4_lv, fast, late, grade, grade_diff, rating, delux_rating, delux_rating_diff, grade_pic_s,
                 notes_tap_cp, notes_tap_p, notes_tap_great, notes_tap_good, notes_tap_miss, notes_hold_cp,
                 notes_hold_p, notes_hold_great, notes_hold_good, notes_hold_miss, notes_slide_cp,
                 notes_slide_p, notes_slide_great, notes_slide_good, notes_slide_miss, notes_touch_cp, notes_touch_p,
                 notes_touch_great, notes_touch_good, notes_touch_miss, notes_break_cp, notes_break_p,
                 notes_break_great, notes_break_good, notes_break_miss, maxcombo, maxsync, level_img_s, name, cache_dt):
        self.vs_rank = vs_rank,
        self.vs_achievement = vs_achievement,
        self.vs_rating = vs_rating,
        self.vs_grade = vs_grade,
        self.chara_0_img_s = chara_0_img_s,
        self.chara_0_star = chara_0_star,
        self.chara_0_lv = chara_0_lv,
        self.chara_1_img_s = chara_1_img_s,
        self.chara_1_star = chara_1_star,
        self.chara_1_lv = chara_1_lv,
        self.chara_2_img_s = chara_2_img_s,
        self.chara_2_star = chara_2_star,
        self.chara_2_lv = chara_2_lv,
        self.chara_3_img_s = chara_3_img_s,
        self.chara_3_star = chara_3_star,
        self.chara_3_lv = chara_3_lv,
        self.chara_4_img_s = chara_4_img_s,
        self.chara_4_star = chara_4_star,
        self.chara_4_lv = chara_4_lv,
        self.fast = fast,
        self.late = late,
        self.grade = grade,
        self.grade_diff = grade_diff,
        self.rating = rating
        self.delux_rating = delux_rating,
        self.delux_rating_diff = delux_rating_diff,
        self.grade_pic_s = grade_pic_s,

        self.notes_tap_cp = notes_tap_cp,
        self.notes_tap_p = notes_tap_p,
        self.notes_tap_great = notes_tap_great,
        self.notes_tap_good = notes_tap_good,
        self.notes_tap_miss = notes_tap_miss,

        self.notes_hold_cp = notes_hold_cp,
        self.notes_hold_p = notes_hold_p,
        self.notes_hold_great = notes_hold_great,
        self.notes_hold_good = notes_hold_good,
        self.notes_hold_miss = notes_hold_miss,

        self.notes_slide_cp = notes_slide_cp,
        self.notes_slide_p = notes_slide_p,
        self.notes_slide_great = notes_slide_great,
        self.notes_slide_good = notes_slide_good,
        self.notes_slide_miss = notes_slide_miss,

        self.notes_touch_cp = notes_touch_cp,
        self.notes_touch_p = notes_touch_p,
        self.notes_touch_great = notes_touch_great,
        self.notes_touch_good = notes_touch_good,
        self.notes_touch_miss = notes_touch_miss,

        self.notes_break_cp = notes_break_cp,
        self.notes_break_p = notes_break_p,
        self.notes_break_great = notes_break_great,
        self.notes_break_good = notes_break_good,
        self.notes_break_miss = notes_break_miss,

        self.maxcombo = maxcombo,
        self.maxsync = maxsync,
        self.level_img_s = level_img_s,
        self.name = name,
        self.cache_dt = cache_dt

    def __repr__(self):
        return '<playlogDetail (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)>' % (
            self.vs_rank, self.vs_achievement, self.vs_rating, self.vs_grade, self.chara_0_img_s, self.chara_0_star,
            self.chara_0_lv, self.chara_1_img_s, self.chara_1_star,
            self.chara_1_lv, self.chara_2_img_s, self.chara_2_star, self.chara_2_lv, self.chara_3_img_s,
            self.chara_3_star, self.chara_3_lv, self.chara_4_img_s, self.chara_4_star, self.chara_4_lv, self.fast,
            self.late, self.grade, self.grade_diff, self.rating, self.delux_rating, self.delux_rating_diff,
            self.grade_pic_s, self.maxcombo, self.maxsync,
            self.level_img_s, self.name, self.cache_dt)

    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        db.session.commit()
        return self


class musicInfo(db.Model):
    __bind_key__ = 'maimai'
    __tablename__ = 'musicinfo_Ver.CH1.11'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(50), nullable=False)
    level_img_s = db.Column(db.VARCHAR(50), nullable=False)
    dx_img_s = db.Column(db.VARCHAR(50))

    music_genre = db.Column(db.VARCHAR(50))
    music_word = db.Column(db.VARCHAR(50))
    music_level = db.Column(db.VARCHAR(50), nullable=False)
    music_version = db.Column(db.VARCHAR(50))

    ver = db.Column(db.VARCHAR(50))
    constant = db.Column(db.FLOAT(2))

    cache_dt = db.Column(db.DateTime, nullable=False)

    def __init__(self, name, level_img_s, dx_img_s, music_genre, music_word, music_level, music_version, ver,
                 cache_dt):
        self.name = name,
        self.level_img_s = level_img_s,
        self.dx_img_s = dx_img_s,
        self.music_genre = music_genre,
        self.music_word = music_word,
        self.music_level = music_level,
        self.music_version = music_version,
        self.ver = ver,
        self.cache_dt = cache_dt

    def __repr__(self):
        return '<musicInfo (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)>' % (
            self.id, self.name, self.level_img_s, self.dx_img_s, self.music_genre, self.music_word, self.music_level,
            self.music_version, self.ver, self.constant, self.cache_dt)

    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
        return self

    def update(self):
        db.session.commit()
        return self


class musicInfo_2021(db.Model, HasId, HasTime):
    __bind_key__ = 'maimai'
    __tablename__ = 'musicinfo_Ver.CH1.11-F'

    name = db.Column(db.VARCHAR(50), nullable=False)
    level_img_s = db.Column(db.VARCHAR(50), nullable=False)
    dx_img_s = db.Column(db.VARCHAR(50))

    music_genre = db.Column(db.VARCHAR(50))
    music_word = db.Column(db.VARCHAR(50))
    music_level = db.Column(db.VARCHAR(50), nullable=False)
    music_version = db.Column(db.VARCHAR(50))

    ver = db.Column(db.VARCHAR(50))

    def __init__(self, name, level_img_s, dx_img_s, music_genre, music_word, music_level, music_version, ver):
        self.name = name,
        self.level_img_s = level_img_s,
        self.dx_img_s = dx_img_s,
        self.music_genre = music_genre,
        self.music_word = music_word,
        self.music_level = music_level,
        self.music_version = music_version,
        self.ver = ver

    def __repr__(self):
        return '<musicInfo_2021 (%s, %s, %s, %s, %s, %s, %s, %s, %s)>' % (
            self.id, self.name, self.level_img_s, self.dx_img_s, self.music_genre, self.music_word, self.music_level,
            self.music_version, self.ver
        )

    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
        return self

    def update(self):
        db.session.commit()
        return self


class musicInfo_2022(db.Model, HasId, HasTime):
    __bind_key__ = 'maimai'
    __tablename__ = 'musicinfo_Ver.CH1.20-H'

    name = db.Column(db.VARCHAR(50), nullable=False)
    level_img_s = db.Column(db.VARCHAR(50), nullable=False)
    dx_img_s = db.Column(db.VARCHAR(50))

    music_genre = db.Column(db.VARCHAR(50))
    music_word = db.Column(db.VARCHAR(50))
    music_level = db.Column(db.VARCHAR(50), nullable=False)
    music_version = db.Column(db.VARCHAR(50))

    ver = db.Column(db.VARCHAR(50))

    def __init__(self, name, level_img_s, dx_img_s, music_genre, music_word, music_level, music_version, ver):
        self.name = name,
        self.level_img_s = level_img_s,
        self.dx_img_s = dx_img_s,
        self.music_genre = music_genre,
        self.music_word = music_word,
        self.music_level = music_level,
        self.music_version = music_version,
        self.ver = ver

    def __repr__(self):
        return '<musicInfo_2022 (%s, %s, %s, %s, %s, %s, %s, %s, %s)>' % (
            self.id, self.name, self.level_img_s, self.dx_img_s, self.music_genre, self.music_word, self.music_level,
            self.music_version, self.ver
        )

    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
        return self

    def update(self):
        db.session.commit()
        return self


class musicInfo_2023(db.Model, HasId, HasTime):
    __bind_key__ = 'maimai'
    __tablename__ = 'musicinfo_Ver.CN1.32-H'

    name = db.Column(db.VARCHAR(50), nullable=False)
    level_img_s = db.Column(db.VARCHAR(50), nullable=False)
    dx_img_s = db.Column(db.VARCHAR(50))

    music_genre = db.Column(db.VARCHAR(50))
    music_word = db.Column(db.VARCHAR(50))
    music_level = db.Column(db.VARCHAR(50), nullable=False)
    music_version = db.Column(db.VARCHAR(50))

    ver = db.Column(db.VARCHAR(50))

    def __init__(self, name, level_img_s, dx_img_s, music_genre, music_word, music_level, music_version, ver):
        self.name = name,
        self.level_img_s = level_img_s,
        self.dx_img_s = dx_img_s,
        self.music_genre = music_genre,
        self.music_word = music_word,
        self.music_level = music_level,
        self.music_version = music_version,
        self.ver = ver

    def __repr__(self):
        return '<musicInfo_2023 (%s, %s, %s, %s, %s, %s, %s, %s, %s)>' % (
            self.id, self.name, self.level_img_s, self.dx_img_s, self.music_genre, self.music_word, self.music_level,
            self.music_version, self.ver
        )

    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
        return self

    def update(self):
        db.session.commit()
        return self


class musicInfo_2024(db.Model, HasId, HasTime):
    __bind_key__ = 'maimai'
    __tablename__ = 'musicinfo_Ver.CN1.40-A'

    name = db.Column(db.VARCHAR(50), nullable=False)
    level_img_s = db.Column(db.VARCHAR(50), nullable=False)
    dx_img_s = db.Column(db.VARCHAR(50))

    music_genre = db.Column(db.VARCHAR(50))
    music_word = db.Column(db.VARCHAR(50))
    music_level = db.Column(db.VARCHAR(50), nullable=False)
    music_version = db.Column(db.VARCHAR(50))

    ver = db.Column(db.VARCHAR(50))

    def __init__(self, name, level_img_s, dx_img_s, music_genre, music_word, music_level, music_version, ver):
        self.name = name,
        self.level_img_s = level_img_s,
        self.dx_img_s = dx_img_s,
        self.music_genre = music_genre,
        self.music_word = music_word,
        self.music_level = music_level,
        self.music_version = music_version,
        self.ver = ver

    def __repr__(self):
        return '<musicInfo_2024 (%s, %s, %s, %s, %s, %s, %s, %s, %s)>' % (
            self.id, self.name, self.level_img_s, self.dx_img_s, self.music_genre, self.music_word, self.music_level,
            self.music_version, self.ver
        )

    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
        return self

    def update(self):
        db.session.commit()
        return self
