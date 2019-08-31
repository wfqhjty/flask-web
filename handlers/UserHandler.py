import json

from handlers.service.UserService import UserService
from utils.Utils import Utils


class UserHandler:

    def getUserList(self, data=None):
        userService = UserService()
        return userService.getUserList()

    def  addUser(self, data):
        userService = UserService()
        # dict_info = json.loads(data.decode("utf-8"))
        dict_info = json.loads(data)
        username = dict_info['username']
        password = dict_info['password']
        phone = dict_info['phone']
        result = userService.addUser(username, password, Utils.getLocalTime(),
                                     phone, 'admin')
        return result

    def getUserByName(self, data):
        userService = UserService()
        dict_info = json.loads(data.decode("utf-8"))
        # dict_info = json.load(data)
        username = dict_info['username']
        result = userService.getUserByName(username)
        return result
