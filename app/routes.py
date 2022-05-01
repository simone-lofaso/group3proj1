from app import myapp_obj, db
from flask import Flask, flash, redirect, request, url_for, render_template
from app.models import User, Products, billingInfo
from app.forms import SaveBillingInfo
login = False

db.create_all()
users = User.query.all()
for u in users:
    print(u)
#db.session.commit()

#This launches to the home page of the website
@myapp_obj.route('/', methods=['GET', 'POST'])
def home():
    
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
                                  secCode=hashed_secCode)
        db.session.add(billingInfo)
        db.session.commit()
        flash('Billing Info Saved')
        return redirect(url_for('home'))
    return render_template('billingInfo.html', title='Billing Info', form=form)

@myapp_obj.route('/viewbillinginfo', methods=['GET', 'POST'])
def viewBillingInfo():
    billinginfo = billingInfo.query.get('user_id')
    return render_template('viewbillinginfo.html', billingInfo=billingInfo)
 
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
