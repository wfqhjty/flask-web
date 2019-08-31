from dbservers.Mysql import PySQL


class UserDao(object):
    def __init__(self):
        pass

    def getUserList(self):
        try:
            sql = "select * from FrameUser"
            return PySQL.get(sql)
        except Exception as e:
            print('ERROR {}'.format(e))
            return []

    def insertUser(self, username, passwd, createdate, phone, deptname):
        try:
            sql = "insert into FrameUser(username,passwd,createdate,phone,deptname) values ('{}','{}','{}','{}','{}') ".format(
                username,
                passwd,
                createdate,
                phone, deptname)
            PySQL.execute(sql)
            return "插入成功"
        except Exception as e:
            print('ERROR {}'.format(e))
            return "插入失败"

    def getUserByName(self, username):
        try:
            sql = "select * from FrameUser where username='" + username + "'"
            return PySQL.getOne(sql)
        except Exception as e:
            print('ERROR {}'.format(e))
            return []
