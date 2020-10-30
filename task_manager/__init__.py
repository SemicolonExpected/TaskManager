from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


# global objects
db = SQLAlchemy()
login = LoginManager()
migrate = Migrate()


def create_app():
    """ Factory to initialize app """
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevelopmentConfig')

    """ Initialize plugins """
    from .models.user import User  # noqa: F401
    from .models.task import Task  # noqa: F401

    db.init_app(app)
    login.init_app(app)
    migrate.init_app(app, db)

    login.login_view = 'login'

    with app.app_context():
        # Register api blueprint and add namespaces
        from task_manager.api import api, user_ns, task_ns

        api.add_namespace(user_ns)
        api.add_namespace(task_ns)

        # Create db tables
        db.create_all()

        return app
