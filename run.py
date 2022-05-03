from app import myapp_obj
from app import os
import sys

debug_mode = False

if '-d' in sys.argv:
    debug_mode = True

myapp_obj.run(debug=debug_mode)
