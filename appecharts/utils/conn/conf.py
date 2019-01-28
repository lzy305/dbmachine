#!/usr/bin/env python  
# encoding: utf-8    
""" 
@version: v1.0 
@author: zy 
@license: Apache Licence  
@contact: 3520771622@qq.com 
@site:  
@software: PyCharm 
@file: conf.py.py 
"""

PRO_ELASTIC_HOSTS = [
    {"host": "192.168.0.176", "port": 9200},
    {"host": "192.168.0.177", "port": 9200},
    {"host": "192.168.0.178", "port": 9200}
]

PRO_ELASTIC_AUTH = ('elastic', '#HiZG!SwzE#=@iH?6H_u')

FIELD_MAPPING = {
    "TINYINT": "Int8",
    "SMALLINT": "Int16",
    "MEDIUMINT": "Int32",
    "INT": "Int32",
    "BIGINT": "Int64",
    "DECIMAL": "Float32",
    "FLOAT": "Float32",
    "DOUBLE": "Float32",
    "DATE": "Date",
    "DATETIME": "DateTime",
    "TIMESTAMP": "DateTime",
    "CHAR": "String",
    "VARCHAR": "String",
    "BLOB": "String",
    "TEXT": "String",
    "LONGBLOB": "String",
    "LONGTEXT": "String",
    "MEDIUMTEXT": "String"
}

SUPORT_DB = ['clickhouse',
             'mysql',
             'postgresql',
             'oracle',
             'httpapi',
             'hive',
             'elastic',
             'clickhouse']
