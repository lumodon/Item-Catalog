#!/usr/bin/env python
from flask import url_for
from flask_app import app
from routes import *
from dotenv import load_dotenv


# Utilize .env environment variables for GoogleAPI
# Citation: July 28th, 2019. https://pypi.org/project/python-dotenv/
load_dotenv()


with app.test_request_context():
    print(url_for('Landing'))
    print(url_for('CategoryListing', category_id=1))


if __name__ == '__main__':
    app.debug = True
    app.secret_key = 'non-production-ready-secret'
    print '\n\n**** FOR TESTING: ****'
    print 'http://localhost:5001/\n**********************\n'
    app.run(host='0.0.0.0', port=5001)
