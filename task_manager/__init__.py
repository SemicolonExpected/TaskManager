import logging
import os
from logging.handlers import RotatingFileHandler

from flask import Flask
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# global objects
db = SQLAlchemy()
login = LoginManager()
migrate = Migrate()
ma = Marshmallow()


def create_app():
    """ Factory to initialize app """
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevelopmentConfig')

    """ Initialize plugins """
    from .models.task import Task  # noqa: F401
    from .models.user import User  # noqa: F401

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    ma.init_app(app)

    login.login_view = 'login'

    with app.app_context():
        # Register api blueprint and add namespaces
        from task_manager.api import api, user_ns, task_ns

        api.add_namespace(user_ns)
        api.add_namespace(task_ns)

        # Create db tables
        db.create_all()

        # Debug
        if not app.debug:
            if not os.path.exists('logs'):
                os.mkdir('logs')
            file_handler = RotatingFileHandler('logs/task_manager.log',
                                               maxBytes=10240, backupCount=10)
            file_handler.setLevel(logging.INFO)
            app.logger.addHandler(file_handler)
            app.logger.setLevel(logging.INFO)
            app.logger.info('Task Manager')

        return app
