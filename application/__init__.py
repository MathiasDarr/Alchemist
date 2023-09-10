from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import json

TEMPLATE_FOLDER = '/application/templates'
STATIC_FOLDER = '/application/static'

db = SQLAlchemy()

def create_app():
    app = Flask(__name__,
                template_folder=TEMPLATE_FOLDER,
                static_folder=STATIC_FOLDER
                )
    from application.views import mount_blueprints
    mount_blueprints(app)
    migrate = Migrate(app, db)
    # database_uri = ""
    #
    app.config.update(
        {
            "SQLALCHEMY_DATABASE_URI": "postgresql://user:password@postgres:5432/jazz"
        }
    )
    db.init_app(app)
    from application.models import Tune
    return app