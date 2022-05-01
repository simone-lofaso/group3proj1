
from app import myapp_obj
from flask import Flask, flash, redirect, request, url_for
from flask import render_template
from app.forms import ItemForm, SearchForm

from app import db
from app.models import User, Item

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

@myapp_obj.route("/create_item", methods=["POST", "GET"])
def item():
    form = ItemForm()
    if request.method == "POST":
        if form.validate_on_submit():
            print('form validated')
            new_item = Item(item_name = form.item_name.data, item_description =form.item_description.data, 
                            item_price = form.item_price.data)
            db.session.add(new_item)
            db.session.commit()
    return render_template('createitem.html', form=form)

@myapp_obj.route("/search", methods=["POST", "GET"])
def search():
    form = SearchForm()
    return render_template('search.html', form=form)

@myapp_obj.route("/results", methods=["POST", "GET"])
def result():
    return render_template('results.html')
    