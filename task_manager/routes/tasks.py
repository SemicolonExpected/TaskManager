from flask import make_response, render_template, jsonify, flash
from flask import redirect

from sqlalchemy import func
#from sqlalchemy import case

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
    if not form.validate_dates():
        flash('Start date must be before End date.')
        return make_response(render_template("createTask.html", form=form))
    if form.validate_on_submit():
        new_task = Task(title=form.title.data,
                        priority=form.priority.data,
                        description=form.description.data,
                        start_time=form.start_date.data,
                        end_time=form.end_date.data,
                        user_id=current_user.id)

        try:
            db.session.add(new_task)
            db.session.flush()

            new_assignment = Assignment(time_added=datetime.today(),
                                        user_id=current_user.id,
                                        task_id=new_task.id)
            db.session.add(new_assignment)
        except Exception as e:
            flash("Exception occured: Unable to add task.")
            print(e)
            db.session.rollback()
        else:
            db.session.commit()
            flash("Task created!")
            return redirect(f'/dashboard')  # noqa: F541
    else:
        flash("Invalid form. Please try again.")
    return make_response(
        render_template("createTask.html", form=form))


def model_fetch_task(task_id):
    task = Task.query.filter_by(user_id=current_user.id).order_by(func.coalesce(Task.start_time, Task.end_time), Task.end_time)
    '''task = Task.query.filter_by(user_id=current_user.id).order_by(
                case((Task.start_time is None, Task.end_time), Task.start_time))'''
    task_schema = TaskSchema(many=True)
    output = task_schema.dump(task)
    return jsonify({'task': output})


def model_get_update_task(task_id):
    """SHOW UPDATE TASK PAGE"""
    task = Task.query.get_or_404(task_id)
    form = CreateTaskForm()
    return make_response(render_template("updateTask.html",
                                         form=form, task=task))


def model_post_update_task(task_id):
    """UPDATE TASK"""
    form = CreateTaskForm()
    task = Task.query.get_or_404(task_id)
    if not form.validate_dates():
        flash('Start date must be before End date.')
        return make_response(
            render_template("updateTask.html", task=task, form=form))
    if form.validate_on_submit():
        try:
            task.title = form.title.data
            task.description = form.description.data
            task.priority = form.priority.data
            task.start_time = form.start_date.data
            task.end_time = form.end_date.data

        except Exception as e:
            flash("Exception occured: Unable to update task.")
            print(e)
            db.session.rollback()
        else:
            db.session.commit()
            flash("Task updated!")
            return redirect(f'/dashboard')  # noqa: F541
    else:
        flash("Invalid form. Please try again.")
    return make_response(
        render_template('updateTask.html', title='Create Task',
                        task=task, form=form))


def model_delete_task(task_id):
    '''
    DELETE TASK
    '''
    task_id = str(task_id).split(",")

    try:
        # simulate a cascading delete
        for i in range(len(task_id)):
            task_to_delete = Task.query.get_or_404(int(task_id[i]))

            assign = Assignment.query.filter_by(task_id=int(task_id[i]))
            [db.session.delete(item) for item in assign]
            db.session.flush()
            db.session.delete(task_to_delete)

    except Exception as e:
        if len(task_id) > 1:
            flash("There was a problem deleting the tasks")
        else:
            flash("There was a problem deleting that task")
        print(e)
        db.session.rollback()
    else:
        db.session.commit()
        if len(task_id) > 1:
            flash("Tasks Deleted!")
        else:
            flash("Task Deleted!")

    return redirect(f'/dashboard')  # noqa: F541
