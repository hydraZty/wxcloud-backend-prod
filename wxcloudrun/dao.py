import json
import logging

from sqlalchemy.exc import OperationalError

from wxcloudrun import db
from wxcloudrun.model import Counters, Users

# 初始化日志
logger = logging.getLogger('log')

def query_user_by_openid(openid):
    """
    根据 openid 查询 Users 实体
    :param openid: 接口 header 里获取到的 openid
    :return: Users实体
    """
    try:
        logger.info("openid= {}".format(openid))
        logger.info("user= {}".format(json.dumps(Users.filter(Users.id == 2).first().to_dict)))

        return db.session.query(Users).filter_by(openid = openid).first()
    except OperationalError as e:
        logger.info("query_userbyopenid errorMsg= {} ".format(e))
        return None

def insert_user(user):
    """
    插入一个Users实体
    :param user: Users
    """
    try:
        db.session.add(user)
        db.session.commit()
    except OperationalError as e:
        logger.info("insert_user errorMsg= {} ".format(e))


def update_user_by_openid(user):
    """
    根据ID更新counter的值
    :param counter实体
    """
    try:
        user = query_user_by_openid(user.openid)
        if user is None:
            return
        db.session.flush()
        db.session.commit()
    except OperationalError as e:
        logger.info("update_user_by_openid errorMsg= {} ".format(e))

def query_counterbyid(id):
    """
    根据ID查询Counter实体
    :param id: Counter的ID
    :return: Counter实体
    """
    try:
        return Counters.query.filter(Counters.id == id).first()
    except OperationalError as e:
        logger.info("query_counterbyid errorMsg= {} ".format(e))
        return None


def delete_counterbyid(id):
    """
    根据ID删除Counter实体
    :param id: Counter的ID
    """
    try:
        counter = Counters.query.get(id)
        if counter is None:
            return
        db.session.delete(counter)
        db.session.commit()
    except OperationalError as e:
        logger.info("delete_counterbyid errorMsg= {} ".format(e))


def insert_counter(counter):
    """
    插入一个Counter实体
    :param counter: Counters实体
    """
    try:
        db.session.add(counter)
        db.session.commit()
    except OperationalError as e:
        logger.info("insert_counter errorMsg= {} ".format(e))


def update_counterbyid(counter):
    """
    根据ID更新counter的值
    :param counter实体
    """
    try:
        counter = query_counterbyid(counter.id)
        if counter is None:
            return
        db.session.flush()
        db.session.commit()
    except OperationalError as e:
        logger.info("update_counterbyid errorMsg= {} ".format(e))
