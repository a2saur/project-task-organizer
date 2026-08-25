from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_moment import Moment


db = SQLAlchemy()
migrate = Migrate()
moment = Moment()

def create_app(config_class = Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.static_folder = config_class.STATIC_FOLDER
    app.template_folder = config_class.TEMPLATE_FOLDER_MAIN

    db.init_app(app)
    migrate.init_app(app, db)
    moment.init_app(app)

    # register blueprints

    from app.main import main_bp
    main_bp.template_folder = config_class.TEMPLATE_FOLDER_MAIN
    app.register_blueprint(main_bp)

    from app.projects import projects_bp
    projects_bp.template_folder = config_class.TEMPLATE_FOLDER_PROJECTS
    app.register_blueprint(projects_bp)

    return app
