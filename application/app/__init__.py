from flask import Flask, render_template
from config import Config

def create_app():

    app = Flask(__name__, static_url_path='/static')
    app.config.from_object(Config)

    return app


app = create_app()

from app.routes import handlers
