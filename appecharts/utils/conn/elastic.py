#!/usr/bin/env python  
# encoding: utf-8    
""" 
@version: v1.0 
@author: zy 
@license: Apache Licence  
@contact: 3520771622@qq.com 
@site:  
@software: PyCharm 
@file: elastic.py 
"""
import json

from records import Record, RecordCollection
from elasticsearch import Elasticsearch

from basic import BasicDbConn
from mixin import ElaMixin


class DbConn(BasicDbConn, ElaMixin):
    def __init__(self, host_ip, host_port=9200, host_user=None, host_password=None, db_type='elastic'):
        self.db = Elasticsearch(hosts=["{}:{}".format(host_ip, host_port)])

    def query(self, sql, columns=None, **kwargs):
        try:
            dsl = json.loads(sql)
            index_name = kwargs.pop("index_name", None)
            type_name = kwargs.pop("type_name", None)
            data_gen = (Record(line['_source'].keys(), line['_source'].values()) for line in
                        self.db.search(body=dsl, index=index_name, doc_type=type_name, _source_include=columns)['hits']['hits'])
            result = RecordCollection(data_gen)
            return result
        except Exception as e:
            print(e)

    def query_file(self):
        pass

    def data_scan(self,
                  sql,
                  index=None,
                  doc_type=None,
                  scroll_time='5m',
                  preserve_order=False,
                  **kwargs):
        n = 1
        if not preserve_order:
            kwargs['search_type'] = 'query_then_fetch'
        rep = self.db.search(body=sql, index=index, doc_type=doc_type, scroll=scroll_time, **kwargs)
        scroll_id = rep.get('_scroll_id')

        if scroll_id is None:
            return None

        first_run = True
        while True:
            if preserve_order and first_run:
                first_run = False
            else:
                rep = self.db.scroll(scroll_id, scroll=scroll_time)

            if not rep['hits']['hits']:
                break

            for hit in rep['hits']['hits']:
                n = n + 1
                yield hit['_source']

            scroll_id = rep.get('_scroll_id')

            if scroll_id is None:
                break


if __name__ == '__main__':
    client = DbConn(host_ip='192.168.0.177', host_port=9200)

    sql = '''
            {"size": 5,
         "query": {
           "match_all": {}
         }
        }
    '''
    kw = {"index_name": "access-log-2018.08.13",
          "type_name": "doc"
          }
    data = client.query(sql, ['request_method', 'brower_name'], **kw )
    for line in data:
        print(line)
    # client = Elasticsearch(hosts='192.168.0.177:9200')
    #
    # dsl = {"size": 5,
    #          "query": {
    #            "match_all": {}
    #          }
    #         }
    #
    # data = client.search(
    #     index="access-log-2018.08.13", doc_type="doc", body= dsl, _source_include=['remote_addr']
    #
    # )
    #
    # for hit in data['hits']['hits']:
    #     print(hit['_source'])
