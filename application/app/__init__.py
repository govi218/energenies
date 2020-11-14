from flask import Flask, render_template
from config import Config


def create_app():

    app = Flask(__name__)
    app.config.from_object(Config) 
    
    return app


app = create_app()

@app.route('/')
def index():
    return render_template('index.html')