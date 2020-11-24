from flask import request, make_response, render_template
from flask import jsonify, redirect
from task_manager.models.task import Task

from task_manager.models.assignment import Assignment
from flask_login import current_user

from task_manager import db
from datetime import datetime, date
from task_manager import ma


class TaskSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Task


def model_get_create_task():
    return make_response(render_template("createTask.html"))


def model_post_create_task():
    task_title = request.form['content']
    task_priority = request.form['priority']
    task_decription = request.form['description']
    if request.form['start_time']:
        task_startTime = request.form['start_time']
        task_st = task_startTime.replace('T', ' ')
        task_start_time = datetime.strptime(task_st, '%Y-%m-%d %H:%M')
    else:
        now = datetime.now()
        task_start_time = now.strftime("%Y-%m-%d %H:%M")
        task_start_time = datetime.strptime(task_start_time, '%Y-%m-%d %H:%M')
    if request.form['end_time']:
        task_endTime = request.form['end_time']
        task_end = task_endTime.replace('T', ' ')
        task_end_time = datetime.strptime(task_end, '%Y-%m-%d %H:%M')
    else:
        # now = datetime.now()
        # task_end_time = now.strftime("%Y-%m-%d %H:%M")
        # task_end_time = datetime.strptime(task_end_time, '%Y-%m-%d %H:%M')
        task_end_time = task_start_time

    if request.form['start_time'] and request.form['end_time']:
        if request.form['start_time'] > request.form['end_time']:
            return "End time is before start time, Please input a valid time."

    new_task = Task(title=task_title, priority=task_priority,
                    description=task_decription,
                    start_time=task_start_time,
                    end_time=task_end_time, user_id=current_user.id)

    try:
        db.session.add(new_task)
        db.session.commit()

        '''Add the new task to assignment with the user who created it'''
        new_assignment = Assignment(time_added=date.today(),
                                    user_id=current_user.id,
                                    task_id=new_task.id)  # since ifDone has a default value I shouldnt need ifDone
        db.session.add(new_assignment)
        db.session.commit()

        # flash('Task successfully added!')

        return redirect('/tasks')
        # later this should return /tasks/new_task.id

    except Exception as e:
        print(e)
        return "Task could not be created :("


def model_fetch_task(task_id):
    # task = Task.query.all()
    task = Task.query.filter_by(user_id=current_user.id)
    task_schema = TaskSchema(many=True)
    output = task_schema.dump(task)
    return jsonify({'task': output})


def model_get_update_task(task_id):
    '''
    SHOW UPDATE TASK PAGE
    '''

    task = Task.query.get_or_404(task_id)
    return make_response(render_template("updateTask.html", task=task))


def model_post_update_task(task_id):
    '''
    UPDATE TASK
    '''

    task = Task.query.get_or_404(task_id)
    task.title = request.form['content']
    task.priority = request.form['priority']
    task.decription = request.form['description']
    if request.form['start_time']:
        task_startTime = request.form['start_time']
        task_st = task_startTime.replace('T', ' ')
        task.start_time = datetime.strptime(task_st, '%Y-%m-%d %H:%M')
    else:
        now = datetime.now()
        task_start_time = now.strftime("%Y-%m-%d %H:%M")
        task.start_time = datetime.strptime(task_start_time, '%Y-%m-%d %H:%M')
    if request.form['end_time']:
        task_endTime = request.form['end_time']
        task_end = task_endTime.replace('T', ' ')
        task.end_time = datetime.strptime(task_end, '%Y-%m-%d %H:%M')
    else:
        # now = datetime.now()
        # task_end_time = now.strftime("%Y-%m-%d %H:%M")
        # task.end_time = datetime.strptime(task_end_time, '%Y-%m-%d %H:%M')
        task.end_time = task.start_time

    if request.form['start_time'] and request.form['end_time']:
        if request.form['start_time'] > request.form['end_time']:
            return "End time is before start time, Please input a valid time."

    try:
        db.session.commit()
        return redirect('/tasks')
        # later this should return /tasks/new_task.id

    except Exception as e:
        print(e)
        return "Task could not be updated :("


def model_delete_task(task_id):
    '''
    DELETE TASK
    '''
    task_to_delete = Task.query.get_or_404(task_id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()

        # Delete associated assignment

        return redirect('/tasks')

    except Exception as e:
        print(e)
        return 'There was a problem deleting that task'
