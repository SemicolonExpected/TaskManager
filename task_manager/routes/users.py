from flask import jsonify, redirect, url_for, make_response, \
    render_template, request
from task_manager.models.user import User, UserSchema
from task_manager import db
from task_manager.forms import UpdateUserForm
user_schema = UserSchema()


def get_user(user_id):
    user = User.query.filter_by(id=int(user_id)).first_or_404()
    user_list = user_schema.dump(user)
    return jsonify({'user': user_list})


#def get_users():
#    users = User.query.all()
#    users_list = user_schema.dump(users, many=True)
#    return jsonify({'users': users_list})


def delete_user(user_id):
    if request.method == "GET":
        return make_response(
            render_template('delete.html', title='Delete'))
    else:
        user = User.query.filter_by(id=int(user_id)).first_or_404()
        user.delete_user()
        return redirect(url_for('index'))


def form_update_user(user_id):
    user = User.query.get_or_404(user_id)
    return make_response(
        render_template("user_account.html",
                        form=UpdateUserForm(user.username, user.email),
                        user=user))


def update_user(user_id):
    user = User.query.get_or_404(user_id)
    form = UpdateUserForm(user.username, user.email)
    if form.validate_on_submit():
        try:
            user.username = form.username.data
            user.email = form.email.data
            user.set_password(form.password.data)

        except Exception as e:
            print(e)
            db.session.rollback()
        else:
            db.session.commit()
            return redirect(f'/dashboard')  # noqa: F541
    else:
        print("Invalid form")
    return make_response(
        render_template('user_account.html',
                        user=user, form=form))
