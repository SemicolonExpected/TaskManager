from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api


# global objects
db = SQLAlchemy()
migrate = Migrate()


def create_app():
    """ Factory to initialize app """
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevelopmentConfig')

    """ Initialize plugins """
    from .models.user import User
    from .models.task import Task

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        # Register api blueprint and add namespaces
        from .routes.endpoints import user_api, task_api

        blueprint = Blueprint('api', __name__, url_prefix='/api')
        api = Api(blueprint, title="RestX APIs", description="")

        app.register_blueprint(blueprint)

        api.add_namespace(user_api)
        api.add_namespace(task_api)

        # Create db tables
        db.create_all()

        # make migrations


        return app
