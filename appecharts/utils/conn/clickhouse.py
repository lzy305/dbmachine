#!/usr/bin/env python  
# encoding: utf-8    
"""
@version: v1.0
@author: zy
@license: Apache Licence
@contact: 3520771622@qq.com
@site:
@software: PyCharm
@file: clickhouse.py
"""

from clickhouse_driver import Client
from records import Record, RecordCollection

from .basic import BasicDbConn
from .mixin import ElaMixin


class DbConn(BasicDbConn, ElaMixin):
    """
    定义数据库查询，批量插入功能
    """
    def __init__(self,
                 host_ip,
                 host_port=9000,
                 host_user=None,
                 host_password=None,
                 db_type='clickhose'
                 ):
        self.host_ip = host_ip
        self.db_type = db_type
        self.host_port = host_port
        self.host_user = host_user
        self.host_password = host_password
        self.conn = Client(self.host_ip)

    def query(self, sql, columns=None, **kwargs):

        rows = self.conn.execute(sql)

        row_gen = (Record(columns, row) for row in rows)

        # Convert psycopg2 results to RecordCollection.
        results = RecordCollection(row_gen)
        # # # Fetch all results if desired.
        # if fetchall:
        #     results.all()

        return results

    def query_file(self):
        pass

    def bulk(self, sql, data):

        """
        :param sql:
        :param data:
        :return:
        """

        # if not isinstance(data, list):
        #     raise "data must be list"

        self.conn.execute(sql, data)
