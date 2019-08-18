from flask import url_for, render_template, send_from_directory, redirect
from database import session, Restaurant, MenuItem
from flask_app import app
from helpers import currency_convert

from flask import session as login_session
import string
import json
import os


CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon')



@app.route('/restaurants/<int:restaurant_id>/')
def RestaurantMenu(restaurant_id):
    if 'username' not in login_session:
        return redirect('/login')
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

    session_user = {}
    if('username' in login_session):
        session_user = {
            'token': login_session['username']
        }

    return render_template(
        'menu.html',
        CLIENT_ID=CLIENT_ID,
        session_user=session_user,
        url_list=url_list,
        items=[item.serialize for item in items],
        restaurant={'name': restaurant.name},
    )


@app.route('/restaurants/<int:restaurant_id>/edit')
def RestaurantMenuEdit(restaurant_id):
    if 'username' not in login_session:
        return redirect('/login')
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

    session_user = {}
    if('username' in login_session):
        session_user = {
            'token': login_session['username']
        }

    return render_template(
        'edit.html',
        CLIENT_ID=CLIENT_ID,
        session_user=session_user,
        url_list=url_list,
        items=[item.serialize for item in items],
        restaurant={'name': restaurant.name, 'id': restaurant_id},
    )


@app.route('/')
def Landing():
    restaurants = session.query(Restaurant).all()

    session_user = {}
    if('username' in login_session):
        session_user = {
            'token': login_session['username']
        }

    return render_template(
        'landing.html',
        CLIENT_ID=CLIENT_ID,
        session_user=session_user,
        restaurants=restaurants
    )
