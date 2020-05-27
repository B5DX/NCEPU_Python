from flask import Flask, url_for, request, redirect

app = Flask(__name__)

# route路由，/代表根目录
@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/index')
def index():
    return 'This is a index page.'

# 接受变量（函数参数必须和route里面对应）
@app.route('/user/<username>')
def showUserProfile(username):
    return f'Hello, {username}.'

# 指定变量类型，string为缺省值
@app.route('/post/<int:post_id>')
def showPost(post_id):
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def showSubpath(subpath):
    return f'Subpath {subpath}'

# 用函数名和参数生成url
with app.test_request_context():
    print(url_for('index'))
    print(url_for('showUserProfile', username='John'))

# 使用模板（必须放在templates子目录里）
from flask import render_template
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

# 缺省时一个路由之回应GET请求
# GET：浏览器告知服务器：只 获取 页面上的信息并发给我。这是最常用的方法。
# POST：浏览器告诉服务器：想在 URL 上 发布 新信息。并且，服务器必须确保 数据已存储且仅存储一次。这是HTML 表单通常发送数据到服务器的方法。
# 还有PUT、HEAD、DELETE、OPTIONS等
# 以下是登录示例
@app.route('/user', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'user' and password == '000':
            return redirect('http:www.baidu.com')

@app.route('/datalist')
def dataList():
    pass

if __name__ == '__main__':
    app.run()