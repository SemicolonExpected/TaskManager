from flask import request  # , make_response, render_template
from flask import jsonify  # , redirect, jsonify, json
from task_manager.models.task import Task
from task_manager import db
from datetime import datetime
from task_manager import ma


class TaskSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Task


def model_get_create_task():
    return {'Show': 'Form'}


def model_post_create_task():
    task_title = request.form['content']
    task_priority = request.form['priority']
    task_decription = request.form['description']
    task_startTime = request.form['start_time']
    task_st = task_startTime.replace('T', ' ')
    task_start_time = datetime.strptime(task_st, '%Y-%m-%d %H:%M')
    task_endTime = request.form['end_time']
    task_end = task_endTime.replace('T', ' ')
    task_end_time = datetime.strptime(task_end, '%Y-%m-%d %H:%M')
    # task_ = request.form['']
    new_task = Task(title=task_title, priority=task_priority,
                    description=task_decription,
                    start_time=task_start_time,
                    end_time=task_end_time)
    try:
        db.session.add(new_task)
        db.session.commit()
        # return redirect('/task/')
        return jsonify({'id': new_task.id,
                        'title': new_task.title,
                        'priority': new_task.priority,
                        'description': new_task.description,
                        'Start time': new_task.start_time,
                        'End Time': new_task.end_time})
    except Exception:
        return Exception


def model_fetch_task(task_id):
    task = Task.query.all()
    # headers = {'Content-Type': 'text/html'}
    # return make_response(render_template('index.html', tasks=task),
    #                      200, headers)
    task_schema = TaskSchema(many=True)
    output = task_schema.dump(task)
    return jsonify({'task': output})


def model_get_update_task(task_id):
    return {'Show': 'Form'}


def model_post_update_task(task_id):
    return {'Update': 'Task'}


def model_delete_task(task_id):
    task_to_delete = Task.query.get_or_404(task_id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        # return redirect('/api/task/')
        return jsonify({'task_id': task_id})
    except Exception:
        return 'There was a problem deleting that task'
    return 'Task %d' % task_id
