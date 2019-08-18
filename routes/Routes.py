from flask import url_for, render_template, send_from_directory
from database import session, Restaurant, MenuItem
from flask_app import app
from helpers import currency_convert

from flask import session as login_session
import random
import string
import os


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon')


# Create anti-forgery state token
@app.route('/login')
def ShowLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    return render_template(
        'login.html',
        client_id=os.getenv('GOOGLE_OAUTH_CLIENT_ID'),
    )
    # return "The current session state is %s" % login_session['state']


@app.route('/restaurants/<int:restaurant_id>/')
def RestaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).first()
    if restaurant == None:
        class placeholderRestaurant:
            id = restaurant_id
            name = "No Restaurant Found with this ID: {}".format(restaurant_id)
        restaurant = placeholderRestaurant
    items = session.query(MenuItem).filter_by(
        restaurant_id=restaurant_id).all()
    for item in items:
        item.price = currency_convert(item.price, True)
    url_list = {
        'landing': url_for('Landing'),
        'restaurant': url_for('RestaurantMenu', restaurant_id=restaurant_id),
    }

    return render_template(
        'menu.html',
        url_list=url_list,
        items=[item.serialize for item in items],
        restaurant={'name': restaurant.name},
    )


@app.route('/restaurants/<int:restaurant_id>/edit')
def RestaurantMenuEdit(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).first()
    if restaurant == None:
        class placeholderRestaurant:
            id = restaurant_id
            name = "No Restaurant Found with this ID: {}".format(restaurant_id)
        restaurant = placeholderRestaurant
    items = session.query(MenuItem).filter_by(
        restaurant_id=restaurant_id).all()
    for item in items:
        item.price = currency_convert(item.price, False)
    url_list = {
        'landing': url_for('Landing'),
        'restaurant': url_for('RestaurantMenu', restaurant_id=restaurant_id),
    }

    return render_template(
        'edit.html',
        url_list=url_list,
        items=[item.serialize for item in items],
        restaurant={'name': restaurant.name, 'id': restaurant_id},
    )


@app.route('/')
def Landing():
    restaurants = session.query(Restaurant).all()
    return render_template(
        'landing.html',
        restaurants=restaurants
    )
