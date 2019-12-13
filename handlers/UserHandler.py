#!/usr/bin/env python
# -*- coding:utf-8 -*-

from handlers.service.UserService import UserService


class UserHandler:

    def getUsersByDeptid(self, deptid):
        userService = UserService()
        result = userService.getUsersByDeptid(deptid)
        return result
