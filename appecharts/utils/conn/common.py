#!/usr/bin/env python  
# encoding: utf-8    
""" 
@version: v1.0 
@author: zy 
@license: Apache Licence  
@contact: 3520771622@qq.com 
@site:  
@software: PyCharm 
@file: jdbc.py 
"""

from records import Database

from basic import BasicDbConn
from mixin import  FieldMappingMixin, ElaMixin


class DbConn(Database, BasicDbConn, FieldMappingMixin, ElaMixin):
    """
    数据库查询, 批量插入
    """

    def __init__(self, host_ip, host_port, host_user=None, host_password=None, db_type='mysql'):

        self.db_info = '{0}:{1}@{2}:{3}'.format(host_user, host_password, host_ip, host_port)
        self.dbtype = db_type

        if self.dbtype == 'mysql':
            self.url = 'mysql+mysqlconnector://{0}/?charset=utf8'.format(self.db_info)

        elif self.dbtype == 'postgresql':
            self.url = 'postgresql+psycopg2://{0}'.format(self.db_info)

        elif self.dbtype == 'oracle':
            self.url = 'oracle+cx_oracle://{0}'.format(self.db_info)
        super(DbConn, self).__init__(db_url=self.url)


# if __name__ == '__main__':
#     client = DbConn(host_ip='192.168.0.198',
#                     host_port=3306,
#                     host_user='root',
#                     host_passwd='RWszjRa5',
#                     db_type='mysql')
#
#     client.mysql_clickhouse('yourong_sr_bank', 'mc_activity', 'Log', 'create_time', 'member_id')