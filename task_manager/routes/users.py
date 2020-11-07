# from flask import Flask
# from flask import request
# from flask_restx import Resource, Api


def model_get_create_user():
    return {'Show': 'Form'}


def model_post_create_user():
    return {'Create': 'User'}


def model_fetch_user(user_id):
    return 'User %d' % user_id


def model_get_update_user(user_id):
    return {'Show': 'Form'}


def model_post_update_user(user_id):
    return {'Update': 'User'}


def model_delete_user(user_id):
    return 'User %d' % user_id
