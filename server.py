from app import create_app
from settings import DEBUG, RELOADER

import sys

args = sys.argv

if len(args) > 1:
    if args[1] == "fake":
        try:
            from data.fakedata import execute
        except:
            pass

create_app().run(debug=DEBUG, reloader=RELOADER)
