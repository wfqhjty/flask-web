#!/usr/bin/env python
# -*- coding:utf-8 -*-

from dbservers.Mysql import PySQL
import json

class Manage():

    def __init__(self):
        pass
    
    def get_depts(self):
        try:
            sql = "select * from framedept"
            return PySQL.get(sql)
        except Exception as e:
            print('ERROR {}'.format(format(e)))
            return []

    def get_users_by_deptid(self, deptid):
        try:
            sql = "select * from frameuser where deptid='" + deptid + "'"
            return PySQL.get(sql)
        except Exception as e:
            print('ERROR {}'.format(e))
            return []

    def step_depts(self):
        depts=self.get_depts()
        list = []
        for i in depts:
            if i['parentid'] is None:
                dictdept = {'id': i['deptid'], 'label': i['deptname']}
                list.append(dictdept)
        for i in list:
            childlist = []
            for j in depts:
                if j['parentid'] == i['id']:
                    dictdept = {'id': j['deptid'], 'label': j['deptname']}
                    childlist.append(dictdept)
            i['children'] = childlist
        return json.dumps(list, ensure_ascii=False)