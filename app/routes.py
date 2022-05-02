from app import myapp_obj, db
from flask import Flask, flash, redirect, request, url_for, render_template
from app.models import User, Products, billingInfo
from app.forms import SaveBillingInfo, PostProductForSale

login = False

db.create_all()
users = User.query.all()
for u in users:
    print(u)
#db.session.commit()
u
#This launches to the home page of the website
@myapp_obj.route('/', methods=['GET', 'POST'])
def home():
    products = Products.query.all()
    return render_template('index.html')

@myapp_obj.route('/billinginfo', methods=['GET', 'POST'])
def billingInfoFunc():
    form = SaveBillingInfo()
    if form.validate_on_submit():
        hashed_secCode = setSecCode(form.password.data)
        billingInfo = billingInfo(name=form.name.data, 
                                  billingAddress=form.billingAddress.data,
                                  cardNumber=form.cardNumber.data,
                                  expirationDate=form.expirationDate.data,
                                  secCode=hashed_secCode,
                                  cardholder=u)
        db.session.add(billingInfo)
        db.session.commit()
        flash('Billing Info Saved')
        return redirect(url_for('home'))
    return render_template('billingInfo.html', title='Billing Info', form=form)

@myapp_obj.route('/postnewproduct', methods=['GET', 'POST'])
def newProductForSale():
    form = PostProductForSale()
    if form.validate_on_submit():
        productForSale = Products(name=form.name.data,
                                  price=form.price.data,
                                  description=form.description.data,
                                  item_image=form.item_image.data,
                                  owner=u)
        db.session.add(productForSale)
        db.session.commit()
        flash('New product for sale')
        return redirect(url_for('home'))
    return render_template('newProductForSale.html', title='Post New Product', form=form)

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
                foundUser = user
                found = True
        
        if found:
            print('valid')
            # print(password)
            verify = User.verify_password(foundUser, password)
            if verify:
                print('matched!')
                return success()
            else:
                print('no match')
        else:
            print('invalid')
            
    return render_template('login.html')


@myapp_obj.route("/success/<string:name>")
def success():
    username = u.username
    return render_template('index.html', login=True, username=username)


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
            
        u = User(username=username, email=email)
        u.set_password(password)
        # print(u)
        db.session.add(u)
        db.session.commit()
        
        return success()
    return render_template('createAccount.html')
