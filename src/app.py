from flask import Flask, render_template, request

from src.views import views
from src.config import config


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(views)


    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/about')
    def about():
        return render_template('about.html')
    
    return app
