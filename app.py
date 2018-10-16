from flask import Flask, request

app = Flask(__name__)


# app.config.from_object('setting.Set') # 配置项

@app.route('/')  # 路由系统，带参数的装饰器，method参数是请求方法，endpoint反向生成URL，其他看源码
def hello_world():

    s = request.remote_addr
    return '你当前的ip地址为'+s


if __name__ == '__main__':
    app.run()
