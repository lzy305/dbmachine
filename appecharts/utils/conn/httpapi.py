#!/usr/bin/env python  
# encoding: utf-8    
""" 
@version: v1.0 
@author: zy 
@license: Apache Licence  
@contact: 3520771622@qq.com 
@site:  
@software: PyCharm 
@file: httpapi.py 
"""
import json
from datetime import datetime, timedelta
import csv

import requests
from records import Record, RecordCollection

from basic import BasicDbConn
from mixin import ElaMixin


class DbConn(BasicDbConn, ElaMixin):
    def __init__(self, host_ip, host_port, host_user=None, host_password=None, db_type='httpapi'):
        self.db_url = '''http://{0}:{1}/api/sql/query?'''.format(host_ip, host_port)
        self.params = {
            "project": "production",
            "format": "json",
            "token": host_password,
        }

    def query(self, sql, columns=None, **kwargs):

        headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                   "Accept-Language": "zh-CN,zh;q=0.8",
                   "Connection": "keep-alive",
                   "Host": "192.168.0.159:8007",
                   "Referer": "http://192.168.0.159:8007/clustering",
                   "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36"
                   }

        self.params.update({"q": sql})

        rep = requests.get(self.db_url, params=self.params, headers=headers)
        content = rep.text.split('\n')

        rows_gen = (Record(json.loads(row).keys(), json.loads(row).values()) for row in content if row.strip())

        results = RecordCollection(rows_gen)

        return results

    def query_file(self):
        pass


if __name__ == "__main__":

    db = DbConn(host_ip='192.168.0.159', host_port=8007, host_user=None, host_password='65dd43a5a43fea4a63b4b0a0ff28ddbdd18c195bb14e9d11d771aa6bbc8b8ac2')
    start_time = datetime.strptime('2017-08-01', '%Y-%m-%d')
    end_time = datetime.strptime('2017-09-30', '%Y-%m-%d')
    headers = ['distinct_id', 'device_id', 'log_time', 'log_ip', 'province', 'city', 'event', 'os', 'app_version',
               'manufacturer', 'screen_width', 'screen_height', 'user_id',
               'browser', 'model', 'network_type', 'total_event_cnt']

    while start_time <= end_time:
        start_day = datetime.strftime(start_time, '%Y-%m-%d')
        next_day = datetime.strftime(start_time + timedelta(days=1), '%Y-%m-%d')
        start_time = start_time + timedelta(days=1)

        sql = '''
                       SELECT $device_id as device_id,
                               distinct_id as distinct_id,
                               user_id as user_id,
                               '{0}' as log_time,
                               $ip as log_ip,
                               $province as province,
                               $city as city,
                               $os as os,
                               $network_type as network_type,
                               $screen_height as screen_height,
                               $screen_width as screen_width,
                               event as event,
                               $model as model,
                               $browser as browser,
                               $app_version as app_version,
                               $manufacturer as manufacturer,
                               count(1) as total_event_cnt
                          FROM events
                         where 1=1
                           and time>='{0}'
                           and time < '{1}'
                           and distinct_id like '110850%'
                    group by $device_id,
                           distinct_id,
                           user_id,
                           $ip ,
                           $province,
                           $city ,
                           $os ,
                           $network_type ,
                           $screen_height,
                           $screen_width,
                           event,
                           $model,
                           $browser,
                           $app_version,
                           $manufacturer
                    '''.format(start_day, next_day)
        rows = [row.as_dict() for row in db.query(sql)]

        with open('/Volumes/zy/data/yrw/user_visit_log_{}.csv'.format(start_day), 'w') as f:
            f_csv = csv.DictWriter(f, headers)
            f_csv.writeheader()
            f_csv.writerows(rows)
