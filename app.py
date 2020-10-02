from flask import Flask, request, render_template
from view.Manage import Manage
import json

from utils.MyEncoder import MyEncoder

app = Flask(__name__)


@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/', methods=['GET'])
def default():
    return render_template('index.html')


@app.route('/stepDepts', methods=['POST'])
def stepDepts():
    manage = Manage()
    result=manage.step_depts()
    return result


@app.route('/getUsersByDeptid', methods=['POST'])
def getUsersByDeptid():
    dict_info = request.get_json()
    deptid = dict_info['deptid']
    manage=Manage()
    result = manage.get_users_by_deptid(str(deptid))
    result = json.dumps(result, cls=MyEncoder)
    return result


if __name__ == '__main__':
    app.run(debug=True)
