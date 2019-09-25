from handlers.dao.DeptDao import DeptDao


class DeptService:

    def __init__(self):
        pass

    def getDepts(self):
        deptDao = DeptDao()
        depts = deptDao.getDepts()
        return depts
