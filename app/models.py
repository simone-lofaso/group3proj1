import base64
import uuid
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True) 
    email = db.Column(db.String(128), index=True, unique=True) 
    password_hash = db.Column(db.String(128))
    cart = db.relationship('Item', backref='buyer')
    
    def set_password(self, password):
        # print(password)
        self.password_hash = hashCode(password)
        
    
    
    def __repr__(self):
        return f'<User {self.username} {self.email} {self.password_hash}>'
   
    def verify_password(self, pwd):
        # print(str(hashCode(pwd)) + " " + (self.password_hash))
        if hashCode(pwd) == int(self.password_hash):
           return True
        return False
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
