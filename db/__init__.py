# #!/usr/bin/env python
# # -*- encoding: utf-8 -*-
# """
# @File    :   __init__.py.py
# @Contact :   pan_qcui@163.com
#
#
# @Modify Time      @Author    @Version    @Desciption
# ------------      -------    --------    -----------
# 2020/9/11 14:10   panqingcui      1.0         None
# """
#
# # import lib
# import os
#
# from flask import Flask
# # import lib
# from flask_sqlalchemy import SQLAlchemy
#
# app = Flask(__name__)
# app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')
# # app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(os.path.dirname(app.root_path), os.getenv('DATABASE_FILE', 'data.db'))
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root:root@localhost:3306/test2"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# db = SQLAlchemy(app)
#
#
