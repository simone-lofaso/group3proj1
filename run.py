from app import myapp_obj
from app import db
from app.models import User

from app import os

if __name__=="__main__":
    myapp_obj.run(host=os.getenv('IP', '0.0.0.0'), 
            port=int(os.getenv('PORT', 5555)))

myapp_obj.run()
