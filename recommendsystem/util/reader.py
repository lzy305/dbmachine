#!/usr/bin/env python  
# encoding: utf-8    
""" 
@version: v1.0 
@author: zy 
@license: Apache Licence  
@contact: 3520771622@qq.com 
@site:  
@software: PyCharm 
@file: reader.py 
"""
import os


def get_user_click(file):
    """
    get
    Args:
        file: input file
    Return:
         dict: key:userid,
               value:[itemid1, itemid2]
    """
    if os.path.exists(file):
        return {}
    user_click = {}
    with open(file, 'rb') as f:
        for line in f:
            item = line.strip().split(',')

            if len(item) < 4:
                continue

            [userid, itemid, rating, timestamp] = item

            if float(rating) < 3.0:
                continue

            if userid not in user_click:
                user_click[userid] = []

            user_click[userid].append(itemid)

    return user_click


def get_item_info(item_file):
    """

    Args:
       item_file: input file

    Return:
         a dict: key itemid,
                 value [title, genres]
    """




