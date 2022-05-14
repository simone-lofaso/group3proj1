from app import myapp_obj
from app import db
from app.models import User

from app import os
import sys

debug_mode = False
<<<<<<< HEAD

if '-d' in sys.argv:
    debug_mode = True
    
if __name__=="__main__":
    myapp_obj.run(host=os.getenv('IP', '0.0.0.0'), 
            port=int(os.getenv('PORT', 8888)))

myapp_obj.run(debug=debug_mode)
=======

if '-d' in sys.argv:
    debug_mode = True

myapp_obj.run(debug=debug_mode)
>>>>>>> a8ddd76749d69f76e767a9d15798cf6ce8364079
