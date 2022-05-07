from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True) 
    email = db.Column(db.String(128), index=True, unique=True) 
    password_hash = db.Column(db.String(128))    
    products = db.relationship('Products', backref='owner', lazy='dynamic')
    billingInfo = db.relationship('BillingInfo', backref='cardholder', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = hashCode(password)
        
    def verify_password(self, pwd):
        if hashCode(pwd) == int(self.password_hash):
           return True
        return False

    def __repr__(self):
        return f'<User {self.username} {self.email} {self.password_hash}>'

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String(64), index=True, unique=False)
    price = db.Column(db.Integer())
    description = db.Column(db.Text)
    item_image = db.Column(db.String(20), default='default.jpg')
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<productsToBuy {self.name} {self.id} {self.price}>'

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

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(64), index=True, unique=True)
    item_description = db.Column(db.String(64), index=True, unique=True)
    item_price = db.Column(db.Float, index=True, unique=True)
    buyer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
