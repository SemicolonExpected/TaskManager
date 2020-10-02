"""
This file will manage interactions with our data store.
At first, it will just contain stubs that return fake data.
Gradually, we will fill in actual calls to our datastore.
"""

#from flask_pymongo import pymongo

#CONNECTION_STRING=

taskid = 1
userid = 1


def fetch_tasks():
    """
    A function to returns all tasks in the data store.
    """
    return {"Task1": 1, "Task2": 2, "Task3": 3}


def create_task(name,optional_priority):
    """
    A function to create a task.
    """
    return taskid


def update_task(taskid):
    """
    A function to update the task based on task ID.
    """
    return taskid


def delete_task(taskid):
    """
    A function to delete the task based on task ID.
    """
    return taskid


def fetch_users():
    """
    A function to returns all users in the data store.
    """
    return {"User1": 1, "User2": 2, "User3": 3}


def create_user(name):
    """
    A function to create a user.
    """
    return userid


def update_userDetails(userid):
    """
    A function to update the user based on user ID.
    """
    return userid


def delete_user(userid):
    """
    A function to delete the user based on user ID.
    """
    return userid
