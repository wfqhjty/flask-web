from flask import Flask, request, render_template
from handlers.UserHandler import UserHandler
import json

app = Flask(__name__)


@app.route('/index', methods=['get'])
def index():
    print("/index")
    return render_template('index.html')


@app.route('/', methods=['get'])
def default():
    return render_template('index.html')


# 用户信息
# 获取所有用户信息
@app.route('/user/getuserlist', methods=['get', 'post'])
def getUserList():
    userHanler = UserHandler()
    result = userHanler.getUserList()
    print(result)
    result = json.dumps(result, ensure_ascii=False)
    print(result)
    return result


# 新增用户
@app.route('/user/adduser', methods=['post'])
def addUser():
    data = request.get_data()
    userHanler = UserHandler()
    result = userHanler.addUser(data)
    return result


# 根据用户名查询
@app.route('/user/getuser', methods=['post'])
def getUserById():
    data = request.get_data()
    userHanler = UserHandler()
    result = userHanler.getUserByName(data)
    result = json.dumps(result, ensure_ascii=False)
    return result


if __name__ == '__main__':
    app.run()
