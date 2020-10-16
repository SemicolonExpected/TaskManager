from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    """ Factory to initialize app """
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevelopmentConfig')

    """ Initialize plugins """
    db.init_app(app)

    with app.app_context():

        # Register blueprints and routes here
        from .routes import tasks, users

        app.register_blueprint(tasks.task_bp)
        app.register_blueprint(users.user_bp)

        # Create db tables
        db.create_all()

        return app
