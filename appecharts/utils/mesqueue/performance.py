#!/usr/bin/env python  
# encoding: utf-8    
""" 
@version: v1.0 
@author: zy 
@license: Apache Licence  
@contact: 3520771622@qq.com 
@site:  
@software: PyCharm 
@file: main.py
@blog:https://www.ctolib.com/topics-103354.html
      http://shift-alt-ctrl.iteye.com/blog/2423162
"""
import uuid
import time
import json

import confluent_kafka
from pykafka import KafkaClient


def confluent_kafka_producer_performance(data, nums=5000):

    topic = 'yrw_event_log'
    conf = {'bootstrap.servers': '192.168.0.164:9092'}
    producer = confluent_kafka.Producer(**conf)
    messages_to_retry = 0

    producer_start = time.time()
    j = 0
    for content in data.run(nums):
        try:
            producer.produce(topic, value=content.encode('utf-8'))
            j = j + 1
            if j % 100000 == 0:
                producer.flush()
        except BufferError as e:
            messages_to_retry += 1

    # hacky retry messages that over filled the local buffer
    for i in range(messages_to_retry):
        producer.poll(0)
        try:
            producer.produce(topic, value=content.encode('utf-8'))
        except BufferError as e:
            producer.poll(0)
            producer.produce(topic, value=content.encode('utf-8'))

    producer.flush()

    print('confluent_kafka produce {0} rows cost {1} s'.format(nums, time.time() - producer_start))


def confluent_kafka_consumer_performance(nums=5000):

    topic = b'event_log'
    msg_consumed_count = 0
    conf = {'bootstrap.servers': '192.168.0.162:9092',
            'group.id': 'zy_consumer',
            'session.timeout.ms': 6000,
            'default.topic.config': {
                'auto.offset.reset': 'earliest'
            }
            }

    consumer = confluent_kafka.Consumer(**conf)

    consumer_start = time.time()
    # This is the same as pykafka, subscribing to a topic will start a background thread
    consumer.subscribe([topic])

    while True:
        print('>>>>>>>>>>>>>>>Starting<<<<<<<<<<<<<<<<<')
        msg = consumer.consume()
        if msg:
            print(msg.value)
            msg_consumed_count += 1

        if msg_consumed_count >= nums:
            break

    consumer_timing = time.time() - consumer_start
    consumer.close()
    print('confluent_kafka_consumer cost:{} s'.format(consumer_timing))


def pykafka_producer_performance(data, use_rdkafka=False, nums=5000):
    # Setup client
    client = KafkaClient(hosts='192.168.0.162:9092')
    topic = client.topics[b'event_log']
    producer = topic.get_producer(use_rdkafka=use_rdkafka)

    produce_start = time.time()
    for content in data.run(nums):
        # Start producing
        producer.produce(content.encode('utf-8'))

    producer.stop()  # Will flush background queue

    print('pykafka produce {0} rows cost {1} s'.format(nums, time.time() - produce_start ))


def pykafka_consumer_performance(conn, use_rdkafka=False, nums=5000):
    # Setup client
    client = KafkaClient(hosts='192.168.0.162:9092,192.168.0.164:9092,192.168.0.166:9092')
    topic = client.topics[b'event_log']

    msg_consumed_count = 0
    datalst = []
    # Consumer starts polling messages in background thread, need to start timer here
    consumer = topic.get_simple_consumer(use_rdkafka=use_rdkafka,
                                         consumer_group=b'zy_consumer_event',
                                         auto_commit_enable=True,
                                         auto_commit_interval_ms=1,

                                         )

    while True:
        msg = consumer.consume()
        if msg:
            # data.append(msg.value, msg.offset)
            try:
                datalst.append(json.loads(msg.value.decode('utf-8')))
                msg_consumed_count += 1
            except Exception as e:
                print(msg.value)
                print(e)

        if msg_consumed_count >= nums:
            try:
                conn.bulk('insert into yourong_sr_bank.yrw_event_log(prov_nm, event_nm, email_nm, access_time, user_id) VALUES',
                          datalst)
                print(msg_consumed_count)
                msg_consumed_count = 0
                datalst = []
            except Exception as e:
                print(e)
                msg_consumed_count = 0
                datalst = []
    consumer.stop()


if __name__ == '__main__':
    confluent_kafka_producer_performance()
    #pykafka_producer_performance(use_rdkafka=False)

    #pykafka_consumer_performance()
    #confluent_kafka_consumer_performance()