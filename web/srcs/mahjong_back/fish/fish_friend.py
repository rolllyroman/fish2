#!/usr/bin/env python
#-*-coding:utf-8 -*-

"""
@Author: $Author$
@Date: $Date$
@version: $Revision$

Description:
捕鱼支付接口模块
"""
from bottle import request,response,error,hook
from fish import fish_app
from web_db_define import *

#from config.config import *
from fish_config import consts
from datetime import datetime
from common import convert_util,web_util,json_util,wechat_util
from common.utilt import allow_cross,getInfoBySid
from urlparse import urlparse
import time
import uuid

@fish_app.post('/friend/invite')
#@allow_cross
def do_inner(redis,session):  
    '''
        发送好友请求
    '''
    msg = request.forms.get("msg","").strip()
    uid = request.forms.get("uid","").strip()
    to_uid = request.forms.get("to_uid","").strip()

    if from_uid in redis.smembers('user:%s:friend:set'%to_uid):
        return {'code':-2,'msg':'您已是对方好友，不能重复发送好友请求！'}

    account = redis.hget('users:%s'%to_uid,'account')
    #if account not in redis.smembers('account4weixin:set'):
    #    return {'code':-1,'msg':'用户不存在！'}


    send_time = str(datetime.now())[:19]

    invite_id = uid + "|" + str(int(time.time()))
    if redis.llen('user:%s:friend:req:list'%to_uid) > 30:
        reids.rpop('user:%s:friend:req:list'%to_uid)

    redis.lpush('user:%s:friend:req:list'%to_uid,invite_id)
    redis.hmset('friend:invite:%s'%invite_id,{
        "from_uid":uid,
        "msg":msg,
        "send_time":send_time,
    })

    return {'code':0,'msg':'发送成功！'}

@fish_app.post('/friend/accept/invite')
#@allow_cross
def do_inner(redis,session):  
    '''
        接受好友申请
    '''
    uid = request.forms.get("uid","").strip()
    from_uid = request.forms.get("from_uid","").strip()
    redis.sadd('user:%s:friend:set'%uid,from_uid)
    return {'code':0,'msg':'添加成功！'}


@fish_app.post('/friend/accept/invite')
#@allow_cross
def do_inner(redis,session):  
    '''
 接受好友申请
    '''
    pass

@fish_app.get('/friend/list')
#@allow_cross
def do_buyCoin(redis,session):  
    '''
        获取好友列表
    '''
    uid = request.GET.get("uid","").strip()
    
