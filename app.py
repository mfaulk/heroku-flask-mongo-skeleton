import os

from flask import Flask
from flask import render_template
from mongoengine import connect
from models import *

import datetime


app = Flask(__name__)
# For Heroku, something like
# heroku config:set APP_SETTINGS=config.ProductionConfig is appropriate.
app.config.from_object(os.environ['APP_SETTINGS'])

#MONGO_URL = os.environ.get('MONGOHQ_URL')
#client = MongoClient(MONGO_URL)

# mongoengine config
DB_NAME = 'test'
connect(DB_NAME)


ross = User(email='Ben@example.com', first_name='Ben', last_name='Bitdiddle').save()

for user in User.objects:
	app.logger.debug(user.first_name)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/robots.txt')
def robots():
    res = app.make_response('User-agent: *\nAllow: /')
    res.mimetype = 'text/plain'
    return res

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
