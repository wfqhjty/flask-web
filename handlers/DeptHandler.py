from handlers.service.DeptService import DeptService


class DeptHandler:

    def __init__(self):
        pass

    def getDepts(self):
        deptService = DeptService()
        result = deptService.getDepts()
        return result
