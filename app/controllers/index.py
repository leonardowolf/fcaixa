# -*- coding: utf-8 -*-
from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    usr={ 'nome':'geraldao', 'idade':50 ,'var': None}
    return render_template('index.html',user = usr)







