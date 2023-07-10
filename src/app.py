from flask import Flask
from flask_bootstrap import Bootstrap5

from src.config import config
from .db import create_db
from .routes import create_routes


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    db = create_db(app)
    create_routes(app, db)
    # app.register_blueprint(views)
    bootstrap = Bootstrap5(app)

    return app


if __name__ == '__main__':
    # reset_tables()
    # create_user()
    # update_user()
    # read_user()
    # delete_user()
    # create_address()
    # read_user()
    app=create_app()
    app.run()