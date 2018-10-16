
from flask import Flask,url_for

app = Flask(__name__)
# app.config.from_object('setting.Set') # 配置项

@app.route('/',redirect_to='http://www.baidu.com') #路由系统，带参数的装饰器，method参数是请求方法，endpoint反向生成URL，其他看源码
def hello_world():
    return 'hello world!'

if __name__ == '__main__':
    app.run()
    app.__call__





