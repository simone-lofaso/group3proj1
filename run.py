from app import myapp_obj

from app import os

if __name__=="__main__":
    myapp_obj.run(host=os.getenv('IP', '0.0.0.0'), 
            port=int(os.getenv('PORT', 3333)))

myapp_obj.run()
