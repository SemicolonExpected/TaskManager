from flask import make_response, render_template, request
from flask import redirect
from task_manager.models.task import Task
from task_manager import db


def model_get_create_task():
    return {'Show': 'Form'}


def model_post_create_task():
    task_content = request.form['content']
    new_task = Task(content=task_content)
    try:
        db.session.add(new_task)
        db.session.commit()
        return redirect('/task/')
    except Exception:
        return 'There was an issue adding your task'
    return {'Create': 'Task'}


def model_fetch_task(task_id):
    task = Task.query.all()
    headers = {'Content-Type': 'text/html'}
    return make_response(render_template('index.html', tasks=task), 200,
                         headers)


def model_get_update_task(task_id):
    return {'Show': 'Form'}


def model_post_update_task(task_id):
    return {'Update': 'Task'}


def model_delete_task(task_id):
    task_to_delete = Task.query.get_or_404(task_id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/task/')
    except Exception:
        return 'There was a problem deleting that task'
    return 'Task %d' % task_id
