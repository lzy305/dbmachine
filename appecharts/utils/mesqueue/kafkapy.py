#!/usr/bin/env python  
# encoding: utf-8    
""" 
@version: v1.0 
@author: zy 
@license: Apache Licence  
@contact: 3520771622@qq.com 
@site:  
@software: PyCharm 
@file: kafkapy.py
@使用pykafka
https://blog.csdn.net/ricky110/article/details/79157043
https://blog.csdn.net/zhidao_wenge/article/details/70037817
https://blog.csdn.net/lmb09122508/article/details/79891460
https://blog.csdn.net/learn_tech/article/details/81115996#(4)%20pykafka%E6%B6%88%E8%B4%B9%E8%80%85api
https://blog.csdn.net/liuxingen/article/details/53335904
"""
from pykafka import KafkaClient
from pykafka.partitioners import RandomPartitioner,HashingPartitioner,GroupHashingPartitioner
from pykafka.common import OffsetType
import random
import json


class ProducerKafka(object):

    def __init__(self, host_ip, host_port, topic):
        self.kafkahost = host_ip
        self.kafkaport = host_port

        self.client = KafkaClient(hosts='{0}:{1}'.format(self.kafkahost, self.kafkaport))
        self.kafkatopic = self.client.topics[topic.encode('utf-8')]

        self.procuder = self.kafkatopic.get_producer(sync=True,
                                                     use_rdkafka=True)

    def desc_topic(self):

        #查看所有分区信息
        print('topic-partitions:{}'.format(self.kafkatopic.partitions))

        #获取最早可用的OFFSET
        print('earliest_offset:{}'.format(self.kafkatopic.earliest_available_offsets()))

        #获取最近可用的OFFSET
        print('latest_offset:{}'.format(self.kafkatopic.latest_available_offsets()))


    def sync_send_json(self, content):
        '''
        同步方式发送消息 并指定
        linger_ms=1,
        partitioner=HashingPartitioner
        '''

        key = str(json.loads(content).get('id', random.randrange(1, 100))).encode('utf-8')
        content = content.encode('utf-8')
        self.procuder.produce(message=content, partition_key=key, timestamp=None)
        print(u'latest_offset:{}'.format(self.kafkatopic.latest_available_offsets()))

    def async_send_json(self, content):
        '''
        异步生产消息
        '''

        key = str(json.loads(content).get('id', random.randrange(1, 100))).encode('utf-8')
        content = content.encode('utf-8')

        self.procuder.produce(message=content, partition_key=key, timestamp=None)
        print(u'latest_offset:{}'.format(self.kafkatopic.latest_available_offsets()))

    def stop(self):
        self.procuder.stop()


class ConsumerKafka(object):
    def __init__(self, host_ip, host_port, topic):
        self.kafkahost = host_ip
        self.kafkaport = host_port
        self.client = KafkaClient(hosts='{0}:{1}'.format(host_ip, host_port))
        self.topic = topic.encode('utf-8')

    def balance_consumer(self):
        kafkatopic = self.client.topics[self.topic]

        consumer = kafkatopic.get_balanced_consumer(b"consumer_group_balanced2",
                                                    managed=True,
                                                    auto_commit_enable=True
                                                        )

        print('该消费组 消费partitions：{}'.format(consumer.partitions))

        while True:
            msg = consumer.consume()
            offset = consumer.held_offsets
            print('{} 前消费者分区offset情况{} '.format(msg.value.decode(), offset))

    def simple_consumer(self):
        kafkatopic = self.client.topics[self.topic]
        consumer = kafkatopic.get_simple_consumer(
            b"zy_simple_consumer",
            auto_commit_enable=True,
            auto_commit_interval_ms=1,
            consumer_id=b'test_id'
        )

        while True:
            msg = consumer.consume()
            offset = consumer.held_offsets
            print('{} 前消费者分区offset情况{} '.format(msg.value.decode(), offset))
        # for message in consumer:
        #     if message:
        #         print("偏移量:{0}, 数据:{1}".format(message.offset, message.value.decode('utf-8')))


if __name__ == '__main__':
    kafclient = ConsumerKafka(host_ip='192.168.0.162',
                              host_port='9092',
                              topic='yrw_event_log'
                              )
    kafclient.simple_consumer()






