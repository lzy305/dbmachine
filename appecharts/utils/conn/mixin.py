#!/usr/bin/env python  
# encoding: utf-8    
""" 
@version: v1.0 
@author: zy 
@license: Apache Licence  
@contact: 3520771622@qq.com 
@site:  
@software: PyCharm 
@file: mixin.py 
"""

from collections import deque, defaultdict
import re

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

from .conf import PRO_ELASTIC_HOSTS, PRO_ELASTIC_AUTH, FIELD_MAPPING


class ElaMixin(object):

    def _data_es(self, sql, columns, op_type="update", **kwargs):
        q = deque([], maxlen=2)
        d = defaultdict(list)
        source_name = "_source" if op_type == "create" else "doc"
        try:
            for line in self.query(sql, columns):
                line = dict(line)
                id = (line.pop("id"), line.pop("index_name"), line.pop("type_name"))
                if q.count(id) == 0:
                    q.append(id)
                d[id].append(line)
                if len(q) == 2:
                    meta = q.popleft()
                    data = d.pop(meta)
                    yield {
                        "_op_type": op_type,
                        "_id": meta[0],
                        "_index": meta[1],
                        "_type": meta[2],
                        source_name: {kwargs["nest_name"]: data} if kwargs.get("nest_name", "") else data[0]
                    }
                meta = q.pop()
                data = d.pop(meta)
                yield {
                        "_op_type": op_type,
                        "_id": meta[0],
                        "_index": meta[1],
                        "_type": meta[2],
                        source_name: {kwargs["nest_name"]: data} if kwargs.get("nest_name", "") else data[0]
                        }
        except Exception as e:
            print(e)

    def insert_es(self, sql, columns, **kwargs):
        try:
            es = Elasticsearch(hosts=PRO_ELASTIC_HOSTS, http_auth=PRO_ELASTIC_AUTH)
            bulk(es, self._data_es(sql, columns, "create", **kwargs))
            return 0
        except Exception as e:
            return e

    def update_es(self, sql, columns, **kwargs):
        try:
            es = Elasticsearch(hosts=PRO_ELASTIC_HOSTS, http_auth=PRO_ELASTIC_AUTH)
            bulk(es, self._data_es(sql, columns,  "update", **kwargs))
            return 0
        except Exception as e:
            return e

    def insup_es(self, sql, columns, **kwargs):
        try:
            es = Elasticsearch(hosts=PRO_ELASTIC_HOSTS, http_auth=PRO_ELASTIC_AUTH)
            for line in self._data_es(sql, columns, "update", **kwargs):
                index_name = line.pop('_index')
                type_name = line.pop('_type')
                _id = line.pop("_id")
                line["doc_as_upsert"] = "true"
                es.update(index=index_name, doc_type=type_name, id=_id, body=line)
            return 0
        except Exception as e:
            print(e)


class FieldMappingMixin(object):

    @staticmethod
    def isnull(fieldnm, fieldtype, fieldnull):

        if fieldnull == 'YES':
            if fieldtype in ['CHAR', 'VARCHAR', 'BLOB', 'TEXT', 'LONGBLOB', 'LONGTEXT']:
                return 'case when {0} is null then "nvl" else {0} end'.format(fieldnm)

            elif fieldtype in ['DATE']:
                return 'case when {0} is null then "1900-01-01" else {0} end'.format(fieldnm)

            elif fieldtype in ['DATETIME', 'TIMESTAMP']:
                return 'case when {0} is null then "1900-01-01 00:00:00" else {0} end'.format(fieldnm)

            else:
                return 'case when {0} is null then 0 else {0} end'.format(fieldnm)
        else:
            return fieldnm

    def mysql_clickhouse(self, table_schema, table_nm, table_engine='MergeTree', table_par=None, table_index=None ):

        sql = '''
         select COLUMN_NAME, 
               upper(DATA_TYPE) as DATA_TYPE,
               upper(IS_NULLABLE) AS IS_NULLABLE
           from information_schema.COLUMNS
         where TABLE_SCHEMA ="{0}"
            and TABLE_NAME = "{1}"
            order by ORDINAL_POSITION asc
         '''.format(table_schema, table_nm)

        rows = self.query(sql)

        ddl_fields = (chr(10)+',').join([" ".join((row.COLUMN_NAME, FIELD_MAPPING.get(row.DATA_TYPE))) for row in rows])

        query_fields = (chr(10)+',').join([self.isnull(row.COLUMN_NAME, row.DATA_TYPE, row.IS_NULLABLE) for row in rows])

        if re.match('MergeTree',table_engine):
            engine = 'ENGINE='+table_engine + ' PARTITION BY toYYYYMM('+table_par+') ' + ' ORDER BY ' + table_index
        else:
            engine = 'ENGINE=' + table_engine

        ddl_script = 'create table {0}.{1}'.format(table_schema, table_nm) \
                     + chr(10) + '('\
                     + ddl_fields \
                     + ')' + chr(10) \
                     + engine+' ;'

        query_script = 'select '  \
                        + query_fields \
                        + chr(10) \
                        + ' from {0}.{1}'.format(table_schema, table_nm)

        print(ddl_script)
        print(query_script)

    def oracle_clickhouse(self):
        pass

    def hive_clickhouse(self):
        pass

    def postgre_clickhouse(self):
        pass

    def sqlserver_clickhouse(self):
        pass



