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


# 计数表
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

    phoneNumber =db.Column(db.String(20))
    email = db.Column(db.String(150))
    registration_date = db.Column(db.Date)
    last_login_data = db.Column(db.DateTime)

    status = db.Column(db.SmallInteger)

    created_at = db.Column('createdAt', db.TIMESTAMP, nullable=False, default=datetime.now())
    updated_at = db.Column('updatedAt', db.TIMESTAMP, nullable=False, default=datetime.now())

