from dbservers.Mysql import PySQL


class UserDao(object):
    def __init__(self):
        pass

    def getUsersByDeptid(self, deptid):
        try:
            sql = "select * from FrameUser where deptid='" + deptid + "'"
            return PySQL.get(sql)
        except Exception as e:
            print('ERROR {}'.format(e))
            return []
