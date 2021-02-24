from app import create_app
from settings import DEBUG, RELOADER
import os

if os.environ.get('APP_LOCATION') == 'heroku':
    create_app().run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    create_app().run(debug=DEBUG, reloader=RELOADER)
    