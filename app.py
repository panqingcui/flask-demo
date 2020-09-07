from flask import Flask, url_for, escape

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'


@app.route('/user/<name>')
def user_page(name):
    return 'User: %s' % escape(name)


@app.route('/test')
def test_url_for():
    # 下面是一些调用示例（请在命令行窗口查看输出的 URL）：
    print(url_for(''))  # 输出：/

    return 'Test page'


if __name__ == '__main__':
    app.run()
