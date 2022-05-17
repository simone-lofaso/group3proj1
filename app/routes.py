from app import myapp_obj, db
from flask import Flask, flash, redirect, request, url_for, render_template
from app.models import User, Product, BillingInfo, CartProduct
from app.forms import SaveBillingInfo, PostProductForSale, AddToCartForm, ItemDescriptionForm, LoginForm, RemoveFromCart, SearchForm

# This global variable is to check if the website is logged in or not
global login
login = False

# This creates the database and stores the variables in the users variable to keep track of
db.create_all()
users = User.query.all()

# This is to delete all the users from the database [FOR TESTING PURPOSES]
# for user in users:
#     # db.session.delete(user)
# db.session.commit()

# This prints the users going into the program
print(users)

# These globals variables keep track of the user (u) and the username (name) currently being logged in
global u
global name


# This launches to the home page of the website
@myapp_obj.route('/', methods=['GET', 'POST'])
def home():
    u = None
    return render_template('index.html')

# This page launches to the billing info part of the website adding the billing info to the database
@myapp_obj.route('/billinginfo', methods=['GET', 'POST'])
def billingInfoFunc():
    global name
    user = User.query.filter(User.username == name).first()
    form = SaveBillingInfo()
    print('start')
    if form.validate_on_submit():
        print('validated')
        billingInfo = BillingInfo(name=form.name.data,
                                  billingAddress=form.billingAddress.data,
                                  cardNumber=form.cardNumber.data,
                                  expirationDate=form.expirationDate.data,
                                  secCode=form.secCode.data,
                                  user_id=user.id)
        db.session.add(billingInfo)
        db.session.commit()
        flash('Billing Info Saved')
        return redirect(url_for('home'))
    return render_template('billingInfo.html', title='Billing Info', form=form)

# This page routes to the /postnewproduct page and allows the user to add a product to the page on the website.
@myapp_obj.route('/postnewproduct', methods=['GET', 'POST'])
def newProductForSale():
    global name
    user = User.query.filter(User.username == name).first()
    form = PostProductForSale()
    if form.validate_on_submit():
        productForSale = Product(name=form.name.data,
                                  price=form.price.data,
                                  description=form.description.data,
                                  item_image=form.item_image.data,
                                  user_id=user.id)
        db.session.add(productForSale)
        db.session.commit()
        flash('New product for sale')
        return redirect(url_for('home'))
    return render_template('newProductForSale.html', title='Post New Product', form=form)

# This launches to the login page of the website and also checks for the correct username and password with the databse.
# If the username and password are correct it will login and print valid. If not it would print no match/invalid
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

# This method gets run if the page gets logged in successfully. Method gets run ONLY if account() is run successfully
@myapp_obj.route("/success/<string:name>")
def success(username):
    print(username)
    if username != None:
        return render_template('index.html', login=True, username=username)
    else:
        return render_template('index.html')


# This is a helper method that checks if a user exists in a database
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

# This launches the page to the create account page and checks if the email and username can be used. 
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

@myapp_obj.route("/search", methods=["POST", "GET"])
def search():
    form = SearchForm()
    return render_template('search.html', form=form)

@myapp_obj.route("/results", methods=["POST"])
def result():
    form = SearchForm()
    second_form = AddToCartForm()
    to_desc = ItemDescriptionForm()
    if form.validate_on_submit():
        search_name = str(form.search_term.data).strip()
        searched_items = Product.query.filter(Product.name.contains(search_name))
        return render_template('results.html', items = list(searched_items), form = second_form, remove = False, desc = to_desc)

# This happens if the delete account button is clicked and removes the account from the databse.
@myapp_obj.route("/delete", methods=["POST", "GET"])
def delete():
    global name
    print(name)
    users = User.query.all()
    if request.method == "POST":
        User.query.filter(User.username == name).delete()
        db.session.commit()
        users = User.query.all()
        print(users)
        return home()
    return render_template('index.html')

@myapp_obj.route("/cart", methods = ["POST"])
def cart():
    form = LoginForm() 
    second_form=RemoveFromCart()
    remove = eval(form.remove.data)
    if form.validate_on_submit():
        users = User.query.all()
        for user in users:
            if user.username == str(form.username.data):
                found_user : User = user
                if User.verify_password(found_user, str(form.password.data)):
                    if not remove:
                        new_cart_product = CartProduct(product_id = int(form.item_id.data), 
                                                       user_id = found_user.id)
                        db.session.add(new_cart_product)
                        db.session.commit()
                    else:
                        product : Product = Product.query.get(int(form.item_id.data))
                        for cart_product in found_user.cart:
                            if cart_product.product() == product:
                                db.session.delete(cart_product)
                                db.session.commit()
                                break
        items = []
        for cart_product in found_user.cart:
            items.append(cart_product.product())
    return render_template("cart.html", items = items, form = second_form)
    
@myapp_obj.route("/cart_login", methods = ["POST"])
def cart_login():
    add_form = AddToCartForm()
    remove_form = RemoveFromCart()
    login_form = LoginForm()
    if add_form.validate_on_submit() or remove_form.validate_on_submit():
        remove = eval(add_form.remove.data) or eval(remove_form.remove.data)
        item_type = add_form.id.data or remove_form.item_id.data
        item_id = int(item_type)
        return render_template("cartlogin.html", item_id=item_id, form = login_form, remove=str(remove))
    
@myapp_obj.route("/item/<item_id>")
def item_view(item_id):
    product = Product.query.get(item_id)
    return render_template("item.html", item=product)
