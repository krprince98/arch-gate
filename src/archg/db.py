import sqlite3
from flask import current_app, g
import click


def get_db():
    g.db = sqlite3.connect(current_app.config['DATABASE'], detect_types=sqlite3.PARSE_DECLTYPES)
    g.db.row_factory = sqlite3.Row

    return g.db

def create_db():
    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('create-db')
def setup_fresh_db():
    create_db()
    click.echo('New Database Initialized.')

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def before_start(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(setup_fresh_db)

