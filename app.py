import json

from faker import Faker
from flask import Flask, url_for, escape, render_template, jsonify, redirect, request, Response
import os

from flask import Flask
# import lib
from flask_sqlalchemy import SQLAlchemy

# from db.models import Movie


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')
# app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(os.path.dirname(app.root_path), os.getenv('DATABASE_FILE', 'data.db'))
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root:root@localhost:3306/test2"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
# from db.models import Movie
# app = Flask(__name__)

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
tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/todo/api/v1.0/user', methods=['GET'])
def get_user():
    return jsonify(username="kkkk", email="2@163.com")


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
    return render_template('index.html', name=name, movies=movies)


@app.route('/hello')
def hello_world():
    return 'Hello, World!'


@app.route('/user/<name>')
def user_page(name):
    return 'User: %s' % escape(name)


@app.route('/test')
def test_url_for():
    # 下面是一些调用示例（请在命令行窗口查看输出的 URL）：
    print(url_for('hello_world'))  # 输出：/
    movie = Movie.query.first()
    print("------->>>>>title-->%s---%s" % (movie.title, movie.year))
    return redirect(url_for('hello_world'))


@app.route("/add", methods=['POST'])
def add():
    if request.method == 'POST':
        print(request.headers)
        print(type(request.json))
        print(request.json)
        result = request.json['title'] + '___' + request.json['date']
        year = str(request.json['date'])[0:4]
        print(year)
        move = Movie(title=request.json['title'], year=year)
        db.session.add_all([move])
        db.session.commit()
        return str(result)
    else:
        return '<h1>只接受post请求！</h1>'


@app.route("/add/json", methods=['POST', 'GET'])
def add_json():
    if request.method == 'POST':
        return Response(json.dumps(request.json), mimetype='application/json')
    else:
        return '当前类型[%s]' % request.method + ',方法只支持POST'


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8');
        return json.JSONEncoder.default(self, obj)


if __name__ == '__main__':
    app.run(debug=True)
