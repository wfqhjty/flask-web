#!/usr/bin/env python
# -*- coding:utf-8 -*-

from dbservers.Mysql import PySQL


class UserDao(object):
    def __init__(self):
        pass

    def getUsersByDeptid(self, deptid):
        try:
            sql = "select * from frameuser where deptid='" + deptid + "'"
            return PySQL.get(sql)
        except Exception as e:
            print('ERROR {}'.format(e))
            return []
