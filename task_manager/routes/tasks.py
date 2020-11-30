from flask import request, make_response, render_template, url_for
from flask import jsonify, redirect

from task_manager.forms import CreateTaskForm
from task_manager.models.task import Task

from task_manager.models.assignment import Assignment
from flask_login import current_user, login_required

from task_manager import db
from datetime import datetime
from task_manager import ma


class TaskSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Task


def model_get_create_task():
    return make_response(
        render_template("createTask.html", form=CreateTaskForm()))


@login_required
def model_post_create_task():
    form = CreateTaskForm()
    if form.validate_on_submit():
        new_task = Task(title=form.title.data, priority=form.priority.data,
                        description=form.description.data,
                        start_time=form.start,
                        end_time=form.end, user_id=current_user.id)

        try:
            db.session.add(new_task)
            db.session.flush()

            new_assignment = Assignment(time_added=datetime.today(),
                                        user_id=current_user.id,
                                        task_id=new_task.id)
            db.session.add(new_assignment)
        except Exception as e:
            print(e)
            db.session.rollback()
        else:
            db.session.commit()
            return redirect(url_for('view_task'))
    return make_response(
        render_template('createTask.html', title='Create Task', form=form))


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
