import os
from flask import Flask, g
from werkzeug.utils import find_modules, import_string
from missive.models import db


def create_app(config=None):
    app = Flask('missive')

    app.config.update(dict(
        DATABASE=os.path.join(app.root_path, 'missive.db'),
        DEBUG=True,
        SECRET_KEY=b'bv!l?l:*vH!&tFA+iNI',
        USERNAME='admin',
        PASSWORD='default'
    ))
    #app.config.update(config or {})
    #app.config.from_envvar('MISSIVE_SETTINGS', silent=True)

    register_blueprints(app)
    register_teardowns(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///missive.db'

    db.app = app
    db.init_app(app)

    #if not hasattr(g, 'db'):
    #    g.db = db
    #app.shell_context_processor({'app': app})

    return app

def register_blueprints(app):
    for name in find_modules('missive.blueprints'):
        mod = import_string(name)
        if hasattr(mod, 'bp'):
            app.register_blueprint(mod.bp)
    return None

def register_teardowns(app):
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db.session.remove()

def setup_database(app):
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    app = create_app()
    # Because this is just a demonstration we set up the database like this.
    if not os.path.isfile('missive.db'):
      setup_database(app)
    #app.run()