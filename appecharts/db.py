#!/usr/bin/env python  
# encoding: utf-8    
""" 
@version: v1.0 
@author: zy 
@license: Apache Licence  
@contact: 3520771622@qq.com 
@site:  
@software: PyCharm 
@file: choose.py 
"""
import importlib
from utils.conn.conf import SUPORT_DB


def choose(dbtype, host_ip, host_port, host_user=None, host_password=None):
    dbtype = dbtype.lower()

    if dbtype not in SUPORT_DB:
        raise 'Not support db {0}, Current support {1}'.format(dbtype, SUPORT_DB)

    if dbtype in ["mysql", "postgresql", "oracle"]:
        packagenm = 'common'
    else:
        packagenm = dbtype

    package = importlib.import_module('utils.conn.{0}'.format(packagenm))
    db = package.DbConn(host_ip, host_port, host_user, host_password, dbtype)
    return db


# if __name__ == '__main__':
#     # 测试 连接 clickhouse
#     client = choose(dbtype='clickhouse', host_ip='192.168.0.164', host_port=9000)
#     data = client.query(sql='''select os,
#                          count(1) as logs,
#                          uniq(distinct_id) as users
#                          from yourong.yrw_member_visit_log group by os''',
#                                          columns =["x", "logs", "users"])
#
#     # for line in data:
#     #     print(line)
#     print([line["x"] for line in data])
#     print([line["logs"] for line in data])
#     print([line["users"] for line in data])

    # 测试 连接 mysql  ;  postgresql, oracle同理
    # client = db(dbtype='mysql', host_ip='192.168.0.198', host_port=3306, host_user='root', host_passwd='RWszjRa5')
    # print(client.url)
    # data = client.query('''select date_format(tt.transaction_time, '%Y-%m-%d') as stat_day,
    #                            count(1) as total_orders,
    #                            sum(invest_amount) as total_invest_amount
    #                     from yourong_sr_bank.tc_transaction tt
    #                     where tt.transaction_time >= "2018-08-07"
    #                     group by date_format(tt.transaction_time, '%Y-%m-%d') ''',
    #                     columns=["x", "logs"])
    #
    # for line in data:
    #     print(line)

    # 测试 连接 elastic
    # client = db(dbtype='elastic', host_ip='192.168.0.177', host_port='9200', host_user='root', host_passwd='RWszjRa5')
    # sql = '''
    #         {"size": 5,
    #      "query": {
    #        "match_all": {}
    #      }
    #     }
    # '''
    #
    # kw = {"index_name": "access-log-2018.08.13",
    #       "type_name": "doc"
    #       }
    #
    # data = client.query(sql, ['request_method', 'brower_name'], **kw)
    #
    # for line in data:
    #     print(line)

    # 测试Httpapi
    # client = db(dbtype='httpapi', host_ip='192.168.0.159', host_port=8007, host_user=None, host_passwd='65dd43a5a43fea4a63b4b0a0ff28ddbdd18c195bb14e9d11d771aa6bbc8b8ac2')
    # client.query()
    #








