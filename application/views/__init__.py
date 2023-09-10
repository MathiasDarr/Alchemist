from application.views.base import blueprint

def mount_blueprints(app):
    app.register_blueprint(blueprint)