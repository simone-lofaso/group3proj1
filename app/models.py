from app import db

#Creates the User and its attributes
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True) 
    email = db.Column(db.String(128), index=True, unique=True) 
    password_hash = db.Column(db.String(128))
    cart = db.relationship('CartProduct', backref='buyer')
    products = db.relationship('Product', backref='owner', lazy='dynamic')
    billingInfo = db.relationship('BillingInfo', backref='cardholder', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = hashCode(password)
        
    def verify_password(self, pwd):
        if hashCode(pwd) == int(self.password_hash):
           return True
        return False

    def __repr__(self):
        return f'<User {self.username} {self.email} {self.password_hash}>'

#Creates the product and its attributes, connected to user
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String(64), index=True, unique=False)
    price = db.Column(db.Integer())
    description = db.Column(db.Text)
    item_image = db.Column(db.String(500), default='default.jpg')
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    cart = db.relationship('CartProduct')
    
    def __repr__(self):
        return f'<productsToBuy {self.name} {self.id} {self.price}>'
    
class CartProduct(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    product_id = db.Column(db.Integer, db.ForeignKey(Product.id))
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    
    def __repr__(self):
        product : Product = Product.query.get(self.product_id)
        return f'<InCart {product.name}#{self.id} @ {product.price}'
    
    def product(self) -> Product:
        product = Product.query.get(self.product_id)
        return product
    
    def user(self) -> User:
        user = User.query.get(self.product_id)
        return user

#Creates billing info and its attributes, connected to user
class BillingInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    billingAddress = db.Column(db.String(128), index=True)
    cardNumber = db.Column(db.Integer())
    expirationDate = db.Column(db.Date)
    secCode = db.Column(db.String(3))
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<billingInfo {self.name} {self.billingAddress} {self.cardNumber}>'

def hashCode(password):
    salted = 0
    for letter in password:
        salted += ord(letter)
    salted += len(password)
    return salted