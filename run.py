from app import myapp_obj
from app import db
from app.models import User

u = User(username='joann', email='jo@example.com')
print(u)

myapp_obj.run()