
#!/usr/bin/env python
# encoding: utf-8    
""" 
@version: v1.0 
@author: zy 
@license: Apache Licence  
@contact: 3520771622@qq.com 
@site:  
@software: PyCharm 
@file: basic.py 
"""
from abc import ABCMeta, abstractmethod


class BasicDbConn(metaclass=ABCMeta):
    @abstractmethod
    def query(self, sql, columns=None, **kwargs):
        pass

    @abstractmethod
    def query_file(self):
        pass