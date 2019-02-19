#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask,render_template,request
from flask_pymongo import PyMongo
from flask_pymongo import MongoClient

app=Flask(__name__)
app.config["MONGO_DBNAME"]='cluster0'
mongo = MongoClient('mongodb://localhost:27017/')
users=mongo.db.users

info=["First name","Last name","username","specialite","annee","email","matricule","password","confirm password"]
                

@app.route('/',methods=['POST','GET'])
@app.route('/challenges/<wv>',methods=['POST','GET'])
def index(wv=''):
    user={}
    if request.method=='POST':
            for i in info:
                    user[info[i]]=request.form[i]
                    
            user['admin']='False'
            users.insertOne(user)
            return render_template('index.html',Title='Chalenges',info=info,registered=True)
    return render_template('index.html',Title='Challenges',info=info,registered=False)






@app.route('/register')
@app.route('/challenges/register')
def register():
        global info
        if request.method=='POST':
                
                if users.find_one({'username':info['username']}) :
			flash("username already taken","error")
			return render_template("register.html",info=info)
		if users.find_one({'email':info['email']}) :
			flash("email already exist","error")
			return render_template("register.html",info=info)
		if users.find_one({'matricule':info['matricule']}) :
			flash("this matricule is already used ","error")
			return render_template("register.html",info=info)
                info["admin"]='False'
		info["date"] = datetime.utcfromtimestamp(int(time())).strftime('%Y-%m-%d %H:%M:%S')
		users.insert_one(info)
		return redirect(url_for("index"))
        return render_template("register.html",info=info)                      


if __name__ == "__main__":
    app.run(debug='True')
