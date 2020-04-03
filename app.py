from flask import Flask, request, render_template
from handlers.UserHandler import UserHandler
from handlers.DeptHandler import DeptHandler
import json

from utils.MyEncoder import MyEncoder

app = Flask(__name__)


@app.route('/index', methods=['GET'])
def index():
    print("/index")
    return render_template('index.html')


@app.route('/', methods=['GET'])
def default():
    return render_template('index.html')


@app.route('/getDepts', methods=['POST'])
def getDepts():
    deptHandler = DeptHandler()
    result = deptHandler.getDepts()
    result = json.dumps(result, ensure_ascii=False)
    return result


@app.route('/stepDepts', methods=['POST'])
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


@app.route('/getUsersByDeptid', methods=['POST'])
def getUsersByDeptid():
    dict_info = request.get_json()
    deptid = dict_info['deptid']
    userHanler = UserHandler()
    result = userHanler.getUsersByDeptid(str(deptid))
    for i in result:
        print(i)
    result = json.dumps(result, cls=MyEncoder)
    return result


if __name__ == '__main__':
    app.run(debug=True)
