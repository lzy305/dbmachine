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
{'Signature': '', 'City': '杭州', 'EncryChatRoomId': '', 'StarFriend': 0,
'AppAccountFlag': 0, 'MemberCount': 0, 'RemarkPYQuanPin': '',
'SnsFlag': 17, 'AttrStatus': 100453, 'PYQuanPin': 'beita', 'ContactFlag': 3,
'HideInputBarFlag': 0, 'VerifyFlag': 0, 'OwnerUin': 0, 'PYInitial': 'BT',
'NickName': '贝塔', 'Statues': 0, 'Uin': 0, 'IsOwner': 0, 'Province': '浙江',
'Alias': '', 'UserName': '@b593cad398c88ef018e27cb8139dd7950f65c65a9008db08113e31cbdc06e716',
'HeadImgUrl': '/cgi-bin/mmwebwx-bin/webwxgeticon?seq=689492716&username=@b593cad398c88ef018e27cb8139dd7950f65c65a9008db08113e31cbdc06e716&skey=@crypt_7f691798_74dc8df3117a0cff045623c83c9b8660',
'RemarkPYInitial': '', 'ChatRoomId': 0, 'UniFriend': 0,
'MemberList': <ContactList: []>, 'DisplayName': '',
'RemarkName': '', 'KeyWord': '', 'Sex': 1}
"""
import os
import json


import itchat
from aip import AipNlp


itchat.auto_login(hotReload=True)
friends = itchat.get_friends(update=True)
client = AipNlp(appId='10984219',
                apiKey='nnfsI9ndgaq5f6G5G2REl51M',
                secretKey='YUeH8atHyMfNftTXq82LdfjitU7nxlhE'
                )


def friend_data(base_path='/Volumes/zy/data/wx_friend/'):
    file_name = os.path.join(base_path, 'wx_friend.txt')
    with open(file_name, 'w', encoding='utf-8') as f:
        for friend in friends:
            json.dump(friend, f, ensure_ascii=False)


def friend_head_image(base_path='/Volumes/zy/data/wx_friend/images/'):

    for friend in friends:
        friend_name = friend['UserName']

        image_file = os.path.join(base_path, '{}.jpg'.format(friend_name[1:]))

        image_data = itchat.get_head_img(friend_name)

        with open(image_file, 'wb') as f:
            f.write(image_data)


def friend_signature():
    for friend in friends:
        signature = friend['Signature']
        if signature:
            print(client.sentimentClassify(signature))


# friend_data()
# friend_head_image()
friend_signature()
