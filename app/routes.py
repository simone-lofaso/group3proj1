from app import myapp_obj
from flask import Flask
from flask import render_template

from app import db
from app.models import User

login = False

db.create_all()
users = User.query.all()
for u in users:
    print(u)
#db.session.commit()

#This launches to the home page of the website
@myapp_obj.route('/')
def home():
    return render_template('index.html')

#This launches to the login page of the website
@myapp_obj.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['pw']
        flash(username)
        flash(password)
        if password == None or username == None:
            print('invalid')
            return render_template('login.html')
        users = User.query.all()
        found = False
        foundUser = ""
        for user in users:
            print(user.username)
            if(user.username == username):
                foundUser = user
                found = True
        
        if found:
            print('valid')
            verify = foundUser.verify_password(password)
            if verify:
                print('matched!')
            else:
                print('no match')
        else:
            print('invalid')
            
    return render_template('login.html')


@myapp_obj.route("/success")
def success():
    login = True
    return render_template('index.html')

@myapp_obj.route("/account", methods=["POST", "GET"])
def create():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['pw']
        flash(username)
        flash(email)
        flash(password)
        if email == None or password == None or username == None:
            print('invalid')
            return render_template('createAccount.html')
        u = User(username=username, email=email)
        u.set_password(password)
        print(u)
        db.session.add(u)
        db.session.commit()
        return success()
    return render_template('createAccount.html')

