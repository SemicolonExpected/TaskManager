from flask import Flask
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

# global objects
db = SQLAlchemy()
login = LoginManager()
migrate = Migrate()
ma = Marshmallow()
apis = Api()


def create_app(config_name):
    """ Factory to initialize app """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_name)

    """ Initialize plugins """
    from .models.task import Task  # noqa: F401
    from .models.user import User  # noqa: F401
    from .models.assignment import Assignment  # noqa: F401
    from task_manager.api import user_ns, task_ns

    db.init_app(app)
    ma.init_app(app)
    login.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)

    login.login_view = 'login'

    apis.add_namespace(user_ns)
    apis.add_namespace(task_ns)

    with app.app_context():
        # Register api blueprint and add namespaces
        apis.init_app(app)

        # Create db tables
        db.create_all()

        return app
