

from app import myapp_obj
from flask import Flask, flash, redirect, request
from flask import render_template
from app.forms import ItemForm, SearchForm

from app import db
from app.models import User, Item

global login
login = False

db.create_all()
users = User.query.all()
# for user in users:
#     # db.session.delete(user)
print(users)
# db.session.commit()
global u
global name
#This launches to the home page of the website
@myapp_obj.route('/')
def home():
    u = None
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
        foundUser = None
        for user in users:
            # print(user.username)
            if(user.username == username):
                global name
                name = username
                foundUser = user
                found = True
        
        if found:
            print('valid')
            # print(password)
            verify = User.verify_password(foundUser, password)
            if verify:
                print('matched!')
                global login
                login = True
                return success(username)
            else:
                print('no match')
        else:
            print('invalid')
            
    return render_template('login.html')


@myapp_obj.route("/success/<string:name>")
def success(username):
    print(username)
    if username != None:
        return render_template('index.html', login=True, username=username)
    else:
        return render_template('index.html')


#checks if a user exists in a database
def exists(string):
    if "@" in string:
        for user in User.query.all():
            if user.email == string:
                return True
    else:
        for user in User.query.all():
            if user.username == string:
                return True
    return False

@myapp_obj.route("/account", methods=["POST", "GET"])
def account():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['pw']
        flash(username)
        flash(email)
        flash(password)
        
        if email == None or exists(email): 
            print('invalid')
            return render_template('createAccount.html', valid = True, message = "Email is Taken")
        elif password == None: 
            print('invalid')
            return render_template('createAccount.html', valid = True, message = "Type in a password")
        elif username == None or exists(username):
            print('invalid')
            return render_template('createAccount.html', valid = True, message = "Username is taken")
            
        global u
        u = User(username=username, email=email)
        u.set_password(password)
        # print(u)
        db.session.add(u)
        db.session.commit()
        global name
        name = username
        return success(name)
    return render_template('createAccount.html')

@myapp_obj.route("/create_item", methods=["POST", "GET"])
def item():
    form = ItemForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            print('form validated')
            new_item = Item(item_name = form.item_name.data, item_description=form.item_description.data, 
                            item_price = form.item_price.data)
            db.session.add(new_item)
            db.session.commit()
        else:
            print('form not validated')
    return render_template('createitem.html', form=form)

@myapp_obj.route("/search", methods=["POST", "GET"])
def search():
    form = SearchForm()
    return render_template('search.html', form=form)

@myapp_obj.route("/results", methods=["POST"])
def result():
    form = SearchForm()
    if form.validate_on_submit():
        search_name = str(form.search_term.data).strip()
        searched_items = Item.query.filter(Item.item_name.contains(search_name))
        return render_template('results.html', items = list(searched_items))
    
@myapp_obj.route("/delete", methods=["POST", "GET"])
def delete():
    global name
    print(name)
    users = User.query.all()
    # print(name + "\n")
    if request.method == "POST":
        # for user in users:
        #     if user.username == name:
        #         print(user)
        #         db.session.delete(user)
        #         name = None
        User.query.filter(User.username == name).delete()
        db.session.commit()
        
        print(users)
        return home()
    return render_template('index.html')
