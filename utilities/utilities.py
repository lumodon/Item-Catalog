from functools import wraps
from flask import flash, redirect, abort, jsonify, make_response
from flask import session as login_session


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' in login_session:
            return f(*args, **kwargs)
        else:
            flash("Access Not Allowed")
            return redirect('/login')
    return decorated_function


def populate_session():
    if 'username' in login_session:
        # If no gplus id then use email, If no email then hard fail
        return {
            'token': login_session['username'],
            'picture': login_session.get('picture', None),
            'gplus_id': login_session.get('gplus_id', login_session['email']),
        }
    return {
        'gplus_id': 'None',
    }


def render_error(msg, code=400):
    flash(msg)
    return make_response(jsonify({"status": "error", "message": msg}), code)
