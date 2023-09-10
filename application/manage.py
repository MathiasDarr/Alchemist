import flask_migrate
from flask.cli import FlaskGroup
from application import create_app
import click

@click.group(cls=FlaskGroup, create_app=create_app)
def cli():
    pass

@cli.command()
def upgrade():
    flask_migrate.upgrade()