from flask import make_response, render_template
from flask import redirect

from task_manager.forms import CreateTaskForm
from task_manager.models.task import Task

from task_manager.models.assignment import Assignment
from flask_login import current_user, login_required

from task_manager import db
from datetime import datetime
from task_manager import ma

import logging

logger = logging.getLogger(__name__)


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
        new_task = Task(title=form.title.data,
                        priority=form.priority.data,
                        description=form.description.data,
                        start_time=form.start,
                        end_time=form.end,
                        user_id=current_user.id)

        try:
            db.session.add(new_task)
            db.session.flush()

            new_assignment = Assignment(time_added=datetime.today(),
                                        user_id=current_user.id,
                                        task_id=new_task.id)
            db.session.add(new_assignment)
        except Exception as e:
            logging.error(e)
            db.session.rollback()
        else:
            db.session.commit()
            return redirect(f'/dashboard')  # noqa: F541
    else:
        logging.error("Invalid form")
        return redirect(f'/task/create')  # noqa: F541


# def model_fetch_task():
#     task = Task.query.filter_by(user_id=current_user.id)
#     task_schema = TaskSchema(many=True)
#     output = task_schema.dump(task)
#     return jsonify({'task': output})


def model_get_update_task(task_id):
    '''
    SHOW UPDATE TASK PAGE
    '''
    task = Task.query.get_or_404(task_id)
    form = CreateTaskForm()
    return make_response(render_template("updateTask.html",
                                         form=form, task=task))


def model_post_update_task(task_id):
    '''
    UPDATE TASK
    '''
    form = CreateTaskForm()
    task = Task.query.get_or_404(task_id)
    if form.validate_on_submit():
        try:
            task.title = form.title.data
            task.description = form.description.data
            task.priority = form.priority.data
            task.start_time = form.start
            task.end_time = form.end

        except Exception as e:
            print(e)
            db.session.rollback()
        else:
            db.session.commit()
            return redirect(f'/dashboard')  # noqa: F541
    else:
        logging.error("Invalid form")
        return make_response(
            render_template('updateTask.html', title='Create Task',
                            task=task, form=form))


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
