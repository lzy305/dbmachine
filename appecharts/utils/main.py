#!/usr/bin/env python  
# encoding: utf-8    
""" 
@version: v1.0 
@author: zy 
@license: Apache Licence  
@contact: 3520771622@qq.com
@software: PyCharm 
@file: main.py 
"""
from mesqueue.performance import pykafka_consumer_performance, confluent_kafka_producer_performance
from conn.clickhouse import DbConn
from gendata import data


confluent_kafka_producer_performance(data, nums=100)
# conn = DbConn(host_ip='192.168.0.164',
#               host_port=9000,
#               host_user=None,
#               host_password=None,
#               db_type='clickhose'
#               )
#
# pykafka_consumer_performance(conn=conn, nums=10000)