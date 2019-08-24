from flask import url_for, render_template, send_from_directory, redirect
from flask_app import app
from database import session, Category, Item

from dateutil import parser
from datetime import datetime
import string
import json
import os

from utilities import login_required, populate_session

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']


def with_default(data_type, q_id, name):
    query_data = session.query(data_type).filter_by(id=q_id).one_or_none()
    if query_data is None:
        class placeholder:
            def __init__(self):
                self.id = q_id
                self.name = "No {} Found with this ID: {}".format(name, q_id)
        return placeholder()
    return query_data


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon')


@app.route('/categories/<int:category_id>/', methods=['GET'])
def CategoryListing(category_id):
    category = with_default(Category, q_id=category_id, name="Categories")
    items = session.query(Item).filter_by(category_id=category_id).all()

    url_list = {
        'landing': url_for('Landing'),
    }

    return render_template(
        'listing.html',
        CLIENT_ID=CLIENT_ID,
        session_user=populate_session(),
        url_list=url_list,
        items=[item.serialize for item in items],
        category={'name': category.name},
    )


@app.route('/items/<int:item_id>', methods=['GET'])
def ItemView(item_id):
    item = with_default(Item, q_id=item_id, name="Items")
    item_category = session.query(Category) \
        .filter_by(id=item.category_id).one_or_none()
    item.category_name = item_category.name
    item.desc_display = [i for i in item.description.splitlines() if i != '']

    url_list = {
        'landing': url_for('Landing'),
        'edit': url_for('ItemEdit', item_id=item_id),
        'delete': url_for('ItemDelete', item_id=item_id),
        'listing': url_for('CategoryListing', category_id=item_category.id)
    }

    return render_template(
        'item.html',
        CLIENT_ID=CLIENT_ID,
        session_user=populate_session(),
        url_list=url_list,
        item=item,
    )


@app.route('/items/<int:item_id>/edit', methods=['GET'])
@login_required
def ItemEdit(item_id):
    item = with_default(Item, q_id=item_id, name="Items")
    item.category_name = session.query(Category) \
        .filter_by(id=item.category_id).first().name
    categories = session.query(Category).all()

    url_list = {
        'landing': url_for('Landing'),
        'item': url_for('ItemView', item_id=item_id),
    }

    return render_template(
        'itemEdit.html',
        CLIENT_ID=CLIENT_ID,
        session_user=populate_session(),
        url_list=url_list,
        item=item,
        categories=categories,
    )


@app.route('/items/create', methods=['GET'])
@login_required
def ItemCreate():
    categories = session.query(Category).all()

    return render_template(
        'create.html',
        CLIENT_ID=CLIENT_ID,
        session_user=populate_session(),
        categories=categories,
    )


@app.route('/', methods=['GET'])
def Landing():
    categories = session.query(Category).all()
    items = session.query(Item) \
        .order_by(Item.create_date.desc()).limit(10).all()

    def modifyDate(item):
        datetime_obj = parser.parse(item['create_date'])
        item['formatted_datetime'] = datetime_obj.strftime("%c")
        item['category_name'] = next(
            i for i in categories if i.id == item['category_id']).name
        return item

    modified_list = [modifyDate(i.serialize) for i in items]

    url_list = {
        'create': url_for('ItemCreate'),
    }

    return render_template(
        'landing.html',
        CLIENT_ID=CLIENT_ID,
        url_list=url_list,
        session_user=populate_session(),
        categories=categories,
        items=modified_list
    )
