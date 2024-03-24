from datetime import datetime

from wxcloudrun import db


# 计数表
class Counters(db.Model):
    # 设置结构体表格名称
    __tablename__ = 'Counters'

    # 设定结构体对应表格的字段
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, default=1)
    created_at = db.Column('createdAt', db.TIMESTAMP, nullable=False, default=datetime.now())
    updated_at = db.Column('updatedAt', db.TIMESTAMP, nullable=False, default=datetime.now())


# 用户表
class Users(db.Model):
    # 设置结构体表格名称
    __tablename__ = 'weixin_users'

    # 设定结构体对应表格的字段
    id = db.Column(db.Integer, primary_key=True)
    openid = db.Column(db.String(255))
    uuid = db.Column(db.String(255))
    nickname = db.Column(db.String(255))
    avatar_url = db.Column(db.String(255))
    gender = db.Column(db.SmallInteger)

    phone_number =db.Column(db.String(20))
    email = db.Column(db.String(150))
    registration_date = db.Column(db.Date)
    last_login_data = db.Column(db.DateTime)

    status = db.Column(db.SmallInteger)

    created_at = db.Column('created_at', db.TIMESTAMP, nullable=False, default=datetime.now())
    updated_at = db.Column('updated_at', db.TIMESTAMP, nullable=False, default=datetime.now())

    def to_dict(self):
        return {
            'id': self.id,
            'openid': self.openid,
            'uuid': self.uuid,
            'nickname': self.nickname,
            'avatar_url': self.avatar_url,
            'gender': self.gender,
            'phone_number': self.phone_number,
            'email': self.email,
            'registration_date': self.registration_date.isoformat() if self.registration_date else None,
            'last_login_data': self.last_login_data.isoformat() if self.last_login_data else None,
            'status': self.status,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
        }


# 场次表
class Matchs(db.Model):
    # 设置结构体表格名称
    __tablename__ = 'Matchs'

    # 设定结构体对应表格的字段
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    alias = db.Column(db.String(100))
    date = db.Column(db.Date)
    match_icon = db.Column(db.String(255))
    carousel_icon = db.Column(db.String(255))
    finish_time = db.Column(db.Time)
    active = db.Column(db.Boolean)
    index = db.Column(db.Integer)
    location = db.Column(db.String(20))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'alias': self.alias,
            'match_icon': self.match_icon,
            'carousel_icon': self.carousel_icon,
            'date': self.date.isoformat() if self.date else None,
            'finish_time': self.finish_time.isoformat() if self.finish_time else None,
            'active': self.active,
            'index': self.index,
            'location': self.location,
        }
