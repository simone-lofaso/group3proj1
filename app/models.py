from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True) 
    email = db.Column(db.String(128), index=True, unique=True) 
    password_hash = db.Column(db.String(128))
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        print(self.password_hash)

    def __repr__(self):
        return f'<User {self.username} {self.email}>'
   
    def verify_password(self, pwd):
       return check_password_hash(self.password_hash, pwd)
   
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(64), index=True, unique=True)
    item_description = db.Column(db.String(64), index=True, unique=True)
    item_price = db.Column(db.Integer, index=True, unique=True)
