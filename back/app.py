from flask import Flask
from flask import request
from flask_cors import CORS
from flask_restful import Api
from flask_restful import Resource

app = Flask(__name__)
CORS(app)
api = Api(app)


@app.route('/', methods=["GET"])
def index():
    return "Welcome to API v1, try /hello."

@app.route('/name',methods=["POST","GET"])
def get_name():
    if request.method == 'GET':
        return 'arno from GET'
    else:
        return 'arno from POST'

## 在Postman 中测是http://127.0.0.1:8010/userProfile?name=arno
## 前端向后端用GET通过URL发送请求发送请求
@app.route('/userProfile',methods=["GET","POST"])
def get_profile():
    if request.method=="GET":
        name = request.args.get('name','')
        print(name)
        return dict(name='luotuo', fans=100000)
    elif request.method=="POST":
        print(request.form)
        print(request.json)
        print(request.data)
        name=request.json.get('name')
        return name
## 前端向后端发送Json利用POST发送请求
## 前端POST请求http://127.0.0.1:8010/userProfile
## raw文件中写Json代码


class Hello(Resource):
    @staticmethod
    def get():
        return "[get] hello flask"

    @staticmethod
    def post():
        return "[post] hello flask"


api.add_resource(Hello, '/hello')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8010)
