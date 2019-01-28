#!/usr/bin/env python  
# encoding: utf-8    
""" 
@version: v1.0 
@author: zy 
@license: Apache Licence  
@contact: 3520771622@qq.com 
@site:  
@software: PyCharm 
@file: analysis.py 
"""
import os
import json

f = open('/Volumes/zy/data/wx_friend/wx_friend.txt', 'r', encoding='utf-8')

data = json.load(f)

print(data)