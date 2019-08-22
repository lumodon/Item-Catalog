from flask import jsonify, request, abort
from flask import session as login_session
from database import session, Category, Item
from flask_app import app


@app.route('/categories/<int:category_id>/listing/JSON')
def CategoryListingJSON(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    items = session.query(Item).filter_by(category_id=category_id).all()
    return jsonify(Items=[i.serialize for i in items])


@app.route('/items/<int:item_id>/edit',
           methods=['POST'])
def ItemEdit(item_id):
    if 'username' not in login_session:
        abort(401)
    else:
        data = request.get_json(cache=False)
        update_result = session.query(Item).filter_by(id=item_id).update({
            'description': data['description'],
            'name': data['name']})
        return jsonify(message=update_result, response='success')


@app.route('/items/create',
           methods=['POST'])
def ItemCreateAjax():
    if 'username' not in login_session:
        abort(401)
    else:
        data = request.get_json(cache=False)
        print 'Data: '
        print data
        create_result = {'val': 'nothing'}
        category = session.query(Category).filter_by(id=data['category']).one()
        new_item = Item(name=data['name'],
                        description=data['description'],
                        owner_id=login_session['gplus_id'],
                        category=category)
        create_result = session.add(new_item)
        session.commit()
        return jsonify(message=create_result, response='success')


@app.route('/items/<int:item_id>/delete',
           methods=['DELETE'])
def ItemDelete(item_id):
    if 'username' not in login_session:
        abort(401)
    else:
        item = session.query(Item).filter_by(id=item_id).one()
        delete_result = session.delete(item)
        return jsonify(
            message=delete_result,
            response='success')
