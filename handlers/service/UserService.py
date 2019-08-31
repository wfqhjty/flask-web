import jsonify
from handlers.dao.UserDao import UserDao


class UserService:

    def getUserList(self):
        dao = UserDao()
        userlist = dao.getUserList()
        return str(userlist)

    def addUser(self, username, passwd, createdate, phone, deptname):
        dao = UserDao()
        result = dao.insertUser(username, passwd, createdate, phone, deptname)
        return result

    def getUserByName(self, username):
        dao = UserDao()
        user = dao.getUserByName(username)
        return str(user)
