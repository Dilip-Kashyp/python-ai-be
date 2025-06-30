from flask import Flask
from flask import Flask
from flask_cors import CORS


def ai_server():
    app = Flask(__name__)
    CORS(app)  # This enables CORS for all routes and origins
    app.config.from_object("app.config.Config")

    from .routes import main

    app.register_blueprint(main)

    return app
