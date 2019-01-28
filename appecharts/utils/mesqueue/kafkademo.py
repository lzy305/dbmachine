#!/usr/bin/env python  
# encoding: utf-8    
""" 
@version: v1.0 
@author: zy 
@license: Apache Licence  
@contact: 3520771622@qq.com 
@site:  
@software: PyCharm 
@file: kafkademo.py
使用 kafka-python
"""
import sys
import time
import json
import random

from kafka import KafkaConsumer, KafkaProducer


class KafkaPro(object):
    def __init__(self, host_ip, host_port, topic):
        self.kafkahost = host_ip
        self.kafkaport = host_port
        self.kafkatopic = topic
        self.bootstrap_servers = ['{0}:{1}'.format(self.kafkahost, self.kafkaport)]
        self.producer = KafkaProducer(bootstrap_servers=self.bootstrap_servers)

    def send_json(self, content):
        v = content.encode('utf-8')
        k = str(random.randint(1, 100)).encode('utf-8')
        self.producer.send(self.kafkatopic, key=k, value=v)
        self.producer.flush()


class KafkaCon(object):
    def __init__(self, host_ip, host_port, topic, groupid):
        self.kafkahost = host_ip
        self.kafkaport = host_port
        self.kafkatopic = topic
        self.groupid = groupid
        self.consumer = KafkaConsumer(self.kafkatopic,
                                      group_id=self.groupid,
                                      bootstrap_servers=['{0}:{1}'.format(self.kafkahost, self.kafkaport)],
                                      auto_offset_reset='earliest'
                                      )

    def pull_data(self):
        print('Start consumer data')
        for message in self.consumer:
            data = message.value
            print(data.decode('utf-8'))


if __name__ == '__main__':
    consumer = KafkaCon(host_ip='192.168.0.162', host_port=9092, topic='event_log', groupid='group_zy_20180811')
    consumer.pull_data()