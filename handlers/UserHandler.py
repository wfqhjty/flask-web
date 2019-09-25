import json

from handlers.service.UserService import UserService


class UserHandler:

    def getUsersByDeptid(self, deptid):
        userService = UserService()
        result = userService.getUsersByDeptid(deptid)
        return result
