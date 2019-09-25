from flask import Flask, request, render_template
from handlers.UserHandler import UserHandler
from handlers.DeptHandler import DeptHandler
import json

from utils.MyEncoder import MyEncoder

app = Flask(__name__)


@app.route('/index', methods=['get'])
def index():
    print("/index")
    return render_template('index.html')


@app.route('/', methods=['get'])
def default():
    return render_template('index.html')


@app.route('/getDepts', methods=['post'])
def getDepts():
    deptHandler = DeptHandler()
    result = deptHandler.getDepts()
    result = json.dumps(result, ensure_ascii=False)
    print(result)
    return result


@app.route('/stepDepts', methods=['post'])
def stepDepts():
    deptHandler = DeptHandler()
    result = deptHandler.getDepts()
    list = []
    for i in result:
        if i['parentid'] is None:
            dictdept = {'id': i['deptid'], 'label': i['deptname']}
            list.append(dictdept)
    for i in list:
        childlist = []
        for j in result:
            if j['parentid'] == i['id']:
                dictdept = {'id': j['deptid'], 'label': j['deptname']}
                childlist.append(dictdept)
        i['children'] = childlist
    result = json.dumps(list, ensure_ascii=False)
    return result


@app.route('/getUsersByDeptid', methods=['post'])
def getUsersByDeptid():
    data = request.get_data()
    dict_info = json.loads(data.decode("utf-8"))
    deptid = dict_info['deptid']
    userHanler = UserHandler()
    result = userHanler.getUsersByDeptid(str(deptid))
    print(type(result))
    for i in result:
        print(i)
    result = json.dumps(result, cls=MyEncoder)
    print("result=", result)
    return result


if __name__ == '__main__':
    app.run()
