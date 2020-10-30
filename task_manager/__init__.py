from flask import Flask, Blueprint
from flask_migrate import Migrate
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# global objects
db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()


def create_app():
    """ Factory to initialize app """
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevelopmentConfig')

    """ Initialize plugins """
    from .models.user import User  # noqa: F401
    from .models.task import Task  # noqa: F401

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        # Register api blueprint and add namespaces
        from task_manager.api import user_api, task_api

        blueprint = Blueprint('api', __name__, url_prefix='/api')
        api = Api(blueprint, title="RestX APIs", description="")

        app.register_blueprint(blueprint)

        api.add_namespace(user_api)
        api.add_namespace(task_api)

        # Create db tables
        db.create_all()

        return app
