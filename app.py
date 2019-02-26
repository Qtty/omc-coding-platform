#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask,render_template,request,jsonify
from flask_pymongo import PyMongo
from flask_pymongo import MongoClient
from datetime import datetime
from time import time,sleep

app=Flask(__name__)
app.config["MONGO_DBNAME"]='cluster0'
mongo = MongoClient('mongodb://localhost:27017/')
users=mongo.db.users

info=["First name","Last name","username","specialite","annee","email","matricule","password","confirm Password"]


@app.route('/',methods=['POST','GET'])
@app.route('/challenges/<wv>',methods=['POST','GET'])
def index(wv=''):

          #  return render_template('index.html',Title='Chalenges',info=info,registered=True)
    return render_template('index.html',Title='Challenges',info=info,registered=False)

@app.route('/register')
@app.route('/challenges/register')
def register():
        global info
        if request.method=='POST':
		return redirect(url_for("index"))
        return render_template("register.html",info=info)



@app.route('/process',methods=['POST'])
def process():
    user={}
    if request.method=='POST':
        data=request.form
        print(data)
        if users.find_one({'username':data['username']}):
			return """{"msg":"error","type":"username already exist"}"""
        if users.find_one({'email':data['email']}) :
			return """{"msg":"error","type":"email already exist"}"""
        if users.find_one({'matricule':data['matricule']}) :
			return """{"msg":"error","type":"matricule already exist"}"""
        for i in info:
            user[i]=data[i]
        user["admin"]='False'
        user["date"] = datetime.utcfromtimestamp(int(time())).strftime('%Y-%m-%d %H:%M:%S')
        users.insert(user)
        return """{"msg":"success","type":"registered"}"""



if __name__ == "__main__":
    app.run(debug='True')
