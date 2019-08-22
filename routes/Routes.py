from flask import url_for, render_template, send_from_directory, redirect
from database import session, Category, Item
from flask_app import app

from flask import session as login_session
import string
import json
import os


CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']


def populate_session():
    if 'username' in login_session:
        # If no gplus id then use email
        # If no email then hard fail with exception
        return {
            'token': login_session['username'],
            'picture': login_session.get('picture', None),
            'gplus_id': login_session.get('gplus_id', login_session['email'])
        }
    return {}


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon')


@app.route('/categories/<int:category_id>/')
def CategoryListing(category_id):
    if 'username' not in login_session:
        return redirect('/login')
    category = session.query(Category).filter_by(id=category_id).first()
    if category == None:
        class placeholderCategory:
            id = category_id
            name = "No Categories Found with this ID: {}".format(category_id)
        category = placeholderCategory
    items = session.query(Item).filter_by(
        category_id=category_id).all()
    url_list = {
        'landing': url_for('Landing'),
        'category': url_for('CategoryListing', category_id=category_id),
    }

    return render_template(
        'listing.html',
        CLIENT_ID=CLIENT_ID,
        session_user=populate_session(),
        url_list=url_list,
        items=[item.serialize for item in items],
        category={'name': category.name},
    )


@app.route('/category/<int:category_id>/edit')
def CategoryListingEdit(category_id):
    if 'username' not in login_session:
        return redirect('/login')
    category = session.query(Category).filter_by(id=category_id).first()
    if category == None:
        class placeholderCategory:
            id = category_id
            name = "No Categories Found with this ID: {}".format(category_id)
        category = placeholderCategory
    items = session.query(Item).filter_by(
        category_id=category_id).all()
    url_list = {
        'landing': url_for('Landing'),
        'category': url_for('CategoryListing', category_id=category_id),
    }

    return render_template(
        'edit.html',
        CLIENT_ID=CLIENT_ID,
        session_user=populate_session(),
        url_list=url_list,
        items=[item.serialize for item in items],
        category={'name': category.name, 'id': category_id},
    )


@app.route('/items/create')
def ItemCreate():
    if 'username' not in login_session:
        return redirect('/login')
    categories = session.query(Category).all()

    return render_template(
        'create.html',
        CLIENT_ID=CLIENT_ID,
        session_user=populate_session(),
        categories=categories,
    )


@app.route('/')
def Landing():
    categories = session.query(Category).all()
    url_list = {
        'create': url_for('ItemCreate'),
    }

    return render_template(
        'landing.html',
        CLIENT_ID=CLIENT_ID,
        url_list=url_list,
        session_user=populate_session(),
        categories=categories
    )
