#!/usr/bin/env python
# -*- coding:utf-8 -*-

from dbservers.Mysql import PySQL


class DeptDao(object):
    def __init__(self):
        pass

    def getDepts(self):
        try:
            sql = "select * from framedept"
            return PySQL.get(sql)
        except Exception as e:
            print('ERROR {}'.format(format(e)))
            return []
