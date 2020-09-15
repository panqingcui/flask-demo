#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   test_app.py    
@Contact :   pan_qcui@163.com


@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/9/14 14:58   panqingcui      1.0         None
"""

# import lib
import requests

# json_data = {'title': 'this is title', 'date': '2020-10-01'}
# r = requests.post("http://127.0.0.1:5000/add", json=json_data)
# print(r.text)
# r = requests.post("http://127.0.0.1:5000/add/json", json=json_data)
# print(r.text)
# r = requests.get("http://127.0.0.1:5000/add/json", json=json_data)
# print(r.text)

r = requests.get("http://127.0.0.1:5000/hello")
print(r.text)
