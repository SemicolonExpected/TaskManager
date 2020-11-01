from flask import make_response, render_template, request, flash
from flask import redirect, jsonify, json
from task_manager.models.user import User, UserSchema
from task_manager import db
from datetime import datetime


# def model_get_create_user():
#     return {'Show': 'Form'}


# def model_post_create_user():
#     return {'Create': 'User'}

user_schema = UserSchema()


def model_get_user(user_id):
    user = User.query.filter_by(id=int(user_id)).first_or_404()
    if user is None:
        flash("User ID does not exist")
    else:
        return user_schema.dump(user)
        # return 'User %d' % user_id


def model_get_update_user(user_id):
    return {'Show': 'Form'}


def model_post_update_user(user_id):
    return {'Update': 'User'}


def model_delete_user(user_id):
    return 'User %d' % user_id
