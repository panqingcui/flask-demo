from faker import Faker
from flask import Flask, url_for, escape, render_template

app = Flask(__name__)

name = '极客架构'
movies = [
    {'title': 'Camillo Govoni', 'date': '2015-12-24'},
    {'title': '高橋 晃', 'date': '2002-02-07'},
    {'title': 'Carla Ross', 'date': '2017-03-06'},
    {'title': 'Isabella Cagnin', 'date': '2010-11-23'},
    {'title': '山岸 真綾', 'date': '1971-04-09'},
    {'title': 'Teresa Howe', 'date': '1975-01-28'},
    {'title': 'Nathan Davis', 'date': '1970-10-16'},
    {'title': 'Sheila Mcconnell', 'date': '2011-08-26'},
    {'title': '孙博', 'date': '1972-06-18'},
    {'title': 'Angelina Pacillo ', 'date': '2001-01-05'},
]


def get_movies():
    aa = []
    fake = Faker(['it_IT', 'en_US', 'ja_JP', 'zh_CN'])
    for _ in range(10):
        c = "{'title':'%s','date':'%s'}" % (fake.name(), fake.date())
        dict = {}
        dict['title'] = fake.name()
        dict['date'] = fake.date()
        dict['address'] = fake.address()
        # print("{'title':'%s','date':'%s'}," % (fake.name(), fake.date()))
        aa.append(dict)
    return aa

def get_users():
    list = []
    fake = Faker(['en_US', 'ja_JP', 'zh_CN'])
    for _ in range(3):
        c = "{'title':'%s','date':'%s'}" % (fake.name(), fake.date())
        dict = {}
        dict['name'] = fake.name()
        dict['date'] = fake.date()
        dict['address'] = fake.address()
        dict['credit_card'] = fake.credit_card_number()
        # print("{'title':'%s','date':'%s'}," % (fake.name(), fake.date()))
        list.append(dict)
    return list
@app.route('/')
def index():
    print(get_users())
    return render_template('index.html', name=name, movies=get_movies())


@app.route('/hello')
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
