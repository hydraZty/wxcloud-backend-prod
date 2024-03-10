from datetime import datetime
import json
from flask import render_template, request, jsonify
from run import app
from wxcloudrun.dao import delete_counterbyid, insert_user, query_counterbyid, insert_counter, query_user_by_openid, update_counterbyid, update_user_by_openid
from wxcloudrun.model import Counters, Users
from wxcloudrun.response import make_succ_empty_response, make_succ_response, make_err_response
import requests


@app.route('/')
def index():
    """
    :return: 返回index页面
    """
    return render_template('index.html')


@app.route('/api/count', methods=['POST'])
def count():
    """
    :return:计数结果/清除结果
    """

    # 获取请求体参数
    params = request.get_json()

    # 检查action参数
    if 'action' not in params:
        return make_err_response('缺少action参数')

    # 按照不同的action的值，进行不同的操作
    action = params['action']

    # 执行自增操作
    if action == 'inc':
        counter = query_counterbyid(1)
        if counter is None:
            counter = Counters()
            counter.id = 1
            counter.count = 1
            counter.created_at = datetime.now()
            counter.updated_at = datetime.now()
            insert_counter(counter)
        else:
            counter.id = 1
            counter.count += 1
            counter.updated_at = datetime.now()
            update_counterbyid(counter)
        return make_succ_response(counter.count)

    # 执行清0操作
    elif action == 'clear':
        delete_counterbyid(1)
        return make_succ_empty_response()

    # action参数错误
    else:
        return make_err_response('action参数错误')


@app.route('/api/count', methods=['GET'])
def get_count():
    """
    :return: 计数的值
    """
    counter = Counters.query.filter(Counters.id == 1).first()
    return make_succ_response(0) if counter is None else make_succ_response(counter.count)


@app.route('/phone', methods=['POST'])  
def get_phone():  
    # 获取请求头中的 x-wx-openid  
    openid = request.headers.get('x-wx-openid')  
      
    # 构建微信 API 请求 URL  
    api_url = f"http://api.weixin.qq.com/wxa/getopendata?openid={openid}"  
      
    # 准备 POST 请求体  
    cloudid = request.json.get('cloudid')  
    body = {  
        "cloudid_list": [cloudid]  
    }  
      
    # 发起 POST 请求到微信 API  
    response = requests.post(api_url, json=body)  
      
    # 检查请求是否成功  
    if response.status_code == 200:  
        try:  
            # 解析响应数据  
            data_list = response.json().get('data_list', [])  
            if data_list:  
                # 解析手机号信息  
                json_data = data_list[0].get('json')  
                phone_data = json.loads(json_data)  
                phone = phone_data.get('data', {}).get('phoneNumber')  
                  
                # 将手机号返回给客户端  
                # 注意：在实际场景中，应对手机号进行保护处理  
                return jsonify({
                    'phone': phone,
                    'openid': openid,
                    })
        except json.JSONDecodeError as e:  
            # 处理 JSON 解析错误  
            return jsonify({'error': 'Failed to parse JSON data'}), 400  
        except Exception as e:  
            # 处理其他异常  
            return jsonify({'error': 'Internal server error'}), 500  
    else:  
        # 处理微信 API 请求失败的情况  
        return jsonify({
            'error': 'Failed to get phone number from WeChat API',
            'Status code': f'{response.status_code}',
            'Content:': response.text,
            'Encoding': response.encoding
            }), response.status_code
    


#  【用户】相关  #
    
@app.route('/api/user', methods=['POST'])
def create_or_update_user():

    # 获取请求头中的 x-wx-openid  
    openid = request.headers.get('x-wx-openid')
    uuid = request.headers.get('x-wx-unionid')

    nickname = request.json.get('nickname')  
    gender = request.json.get('gender')  
    avatar_url = request.json.get('avatar_url')  
    phoneNumber = request.json.get('phoneNumber')  
    email = request.json.get('email')  


    if not uuid:
        uuid = ''
    user = query_user_by_openid(openid)
    if user is None:
        # 新增用户
        user = Users()
        user.openid = openid
        user.uuid = uuid
        user.nickname = ''
        user.avatar_url = ''
        user.phoneNumber = ''
        insert_user(user)
    else:
        # 更新用户数据
        if uuid:
          user.uuid = uuid
        if nickname:
          user.nickname = nickname
        if avatar_url:
          user.avatar_url = avatar_url
        if gender:
          user.gender = gender
        if phoneNumber:
          user.phoneNumber = phoneNumber
        if email:
          user.email = email
        
        # counter.count += 1
        # counter.updated_at = datetime.now()
        update_user_by_openid(user)
    return make_succ_response(user.to_dict())

@app.route('/api/user', methods=['GET'])
def get_user_info():
    """
    :return: Users
    """
    # 获取请求头中的 x-wx-openid  
    openid = request.headers.get('x-wx-openid')
    print(openid)
    user = query_user_by_openid(openid)
    if user:
      print(user.id)
      return make_succ_response(user.to_dict())
    else:
      return make_succ_response({'openid': openid, 'user': user})
