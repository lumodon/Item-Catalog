from flask import jsonify, request
from database import session, Restaurant, MenuItem
from flask_app import app
from utilities.toaster import Toaster


@app.route('/restaurants/<int:restaurant_id>/menu/JSON')
def restaurantMenuJSON(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()
    return jsonify(MenuItems=[i.serialize for i in items])


@app.route('/restaurants/<int:restaurant_id>/menu/<int:menuitem_id>',
           methods=['POST'])
def restaurantMenuItemEdit(restaurant_id, menuitem_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    data = request.get_json(cache=False)
    update_result = session.query(MenuItem).filter_by(id=menuitem_id).update({
        'price': data['price'],
        'description': data['description'],
        'name': data['name'],
    })
    session.commit()
    return jsonify(message=update_result, response='success')


@app.route('/api/toaster', methods=['POST'])
def persistantToaster():
    data = request.get_json()
    print 'toaster:'
    print Toaster
    print '\ndata:'
    print data
    Toaster['queue'] = data['queue']
    return jsonify(response='success')
