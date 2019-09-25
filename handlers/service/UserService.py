from handlers.dao.UserDao import UserDao


class UserService:

    def getUsersByDeptid(self, deptid):
        dao = UserDao()
        users = dao.getUsersByDeptid(deptid)
        return users
