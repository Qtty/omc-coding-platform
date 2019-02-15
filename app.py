#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
@app.route('/chalenge/<wv>')
def index(wv=''):
    if wv=='':
        return render_template('index.html',Title='Chalenges')



if __name__ == "__main__":
    app.run(debug='True')
