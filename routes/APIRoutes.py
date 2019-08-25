from flask import jsonify, request, abort, flash
from flask import session as login_session
from flask_app import app
from database import session, Category, Item

from utilities import login_required, render_error


@app.route('/categories/<int:category_id>/listing/JSON', methods=['GET'])
def CategoryListingJSON(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    items = session.query(Item).filter_by(category_id=category_id).all()
    return jsonify(Items=[i.serialize for i in items])


@app.route('/items/<int:item_id>/edit',
           methods=['POST'])
@login_required
def ItemSave(item_id):
    s_item = session.query(Item).filter_by(id=item_id)
    item = s_item.one_or_none()

    if item is None:
        return render_error("Item id is invalid", 400)
    if (login_session['gplus_id'] != item.owner_id):
        return render_error("You are not allowed to edit this item", 403)
    else:
        data = request.get_json(cache=False)
        update_result = s_item.update({
            'description': data['description'],
            'name': data['name']})
        session.commit()
        return jsonify(message=update_result, response='success')


@app.route('/items/create', methods=['POST'])
@login_required
def ItemCreateAjax():
    data = request.get_json(cache=False)
    create_result = {'val': 'nothing'}
    category = session.query(Category) \
        .filter_by(id=data['category']).one_or_none()
    if category is None:
        return render_error("Category is invalid", 400)
    else:
        new_item = Item(name=data['name'],
                        description=data['description'],
                        owner_id=login_session['gplus_id'],
                        category=category)
        create_result = session.add(new_item)
        session.commit()
        return jsonify(message=create_result, response='success')


@app.route('/items/<int:item_id>/delete', methods=['POST'])
@login_required
def ItemDelete(item_id):
    item = session.query(Item).filter_by(id=item_id).one_or_none()
    if (login_session['gplus_id'] != item.owner_id):
        return render_error("You are not allowed to delete this item", 403)
    else:
        delete_result = session.delete(item)
        session.commit()
        return jsonify(
            message=delete_result,
            response='success')
