from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# global objects
db = SQLAlchemy()
migrate = Migrate()


def create_app():
    """ Factory to initialize app """
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevelopmentConfig')

    """ Initialize plugins """
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from .routes import api

        app.register_blueprint(api.task_bp)
        app.register_blueprint(api.user_bp)

        return app
