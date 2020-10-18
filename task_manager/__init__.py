from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    """ Factory to initialize app """
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevelopmentConfig')

    """ Initialize plugins """
    db.init_app(app)
    login_manager.init_app(app)

    # login_manager.login_view = 'login'

    with app.app_context():
        # Register blueprints and routes here
        from .routes import tasks, users, auth

        app.register_blueprint(tasks.task_bp)
        app.register_blueprint(users.user_bp)
        # app.register_blueprint(auth.auth_bp)

        # Create models
        db.create_all()

        # compile static assets for dev testing only

        return app
