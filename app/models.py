from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True) 
    email = db.Column(db.String(128), index=True, unique=True) 
    password_hash = db.Column(db.String(128))    
    products = db.relationship('Products', backref = 'owner', lazy = 'dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        print(self.password_hash)
    
    def verify_password(self, pwd):
        return check_password_hash(self.password_hash, pwd)

    def __repr__(self):
        return f'<User {self.username} {self.email}>' 

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String(64), index=True, unique=False)
    price = db.Column(db.Integer())
    description = db.Column(db.Text)
    item_image = db.Column(db.String(20), default='default.jpg')
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<productsToBuy {self.name} {self.id} {self.price}>'

