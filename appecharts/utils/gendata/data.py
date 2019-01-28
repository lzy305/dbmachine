#!/usr/bin/env python  
# encoding: utf-8    
""" 
@version: v1.0 
@author: zy 
@license: Apache Licence  
@contact: 3520771622@qq.com 
@site:  
@software: PyCharm 
@file: data.py
@ 5W1H:
   What  执行什么事情
   where 什么地点执行
   why 为什么执行
   when 什么时间执行
   who 由谁执行
   how  如何执行
   value: 产品的价值
"""

import random
import string
from datetime import datetime, timedelta
import json


EMAIL_SUFFIX = ['qq.com', '163.com', '139.com', '189.cn', '126.com',
                'tom.com', 'aliyun.com', '188.com', 'yeah.net', 'wo.cn']

MOBILE_PREFIX = ['134', '135', '136', '137', '138', '139', '147', '150', '151', '152', '157', '158', '159', '187', '188',
                 '130', '131', '132', '155', '156', '185', '186',
                 '133', '153', '180', '189']

EVENT_NM = ['view', 'order', 'pay', 'withdraw', 'recharge']

PROV_NM = ['北京市', '天津市', '上海市', '重庆市', '河北省', '河南省', '云南省', '辽宁省',
           '黑龙江省', '湖南省', '安徽省', '山东省', '新疆维吾尔', '江苏省', '浙江省', '江西省',
           '湖北省', '广西壮族', '甘肃省', '山西省', '内蒙古', '陕西省', '吉林省', '福建省',
           '贵州省', '广东省', '青海省', '西藏', '四川省', '宁夏回族', '海南省']

HTTP_PROTOCOL = ['http', 'https']

HTTP_DOMAIN = ['www.yrw.com', 'www.mp.weixin.qq.com/s/SKWc9HUpzMmgfCVm7MJiog', 'www.yrw.com/article/noticedetail-1177.html',
               'www.yrw.com/activity/entrance/happysummer', 'www.yrw.com/post/directActivator',
               'www.yrw.com/activity/inviteFriend/2018', 'www.yrw.com/post/bankDepository',
               'www.yrw.com/activity/inviteFriends', 'www.yrw.com/post/newSixGift/index',
               'www.yrw.com/post/dataCenter', 'www.yrw.com/products/projectlist.html',
               'www.yrw.com/about/index.html', 'www.yrw.com/about/recordInformation']


def digit_letters():
    return string.ascii_letters+'_' + string.digits


def email_data():
    return '{0}{1}{2}'.format(''.join(random.sample(digit_letters(),  9)), '@', random.choice(EMAIL_SUFFIX))


def mobile_data():
    return random.choice(MOBILE_PREFIX) + ''.join(random.sample(string.digits, 8))


def event_data():
    return random.choice(EVENT_NM)


def prov_data():
    return random.choice(PROV_NM)


def time_data():
    return str(datetime.now() + timedelta(seconds=random.randrange(1,6000)))


def url_data():
    return random.choice(HTTP_PROTOCOL) + '://'+random.choice(HTTP_DOMAIN)


def run(nums):
    for _ in range(nums):
        params = {}
        event_nm = event_data()

        if event_nm == 'view':
            params.update({"request_url": url_data()})

        yield json.dumps(obj={"user_id": mobile_data(),  "access_time": time_data(),
                               "prov_nm": prov_data(),   "event_nm": event_nm,
                               "email_nm": email_data(), "params": "clickhouse-kafka"}, ensure_ascii=False)


if __name__ == '__main__':
    for line in run(1000000):
        print(line)


