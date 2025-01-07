from flask import Flask

def ai_server():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    from .routes import main
    app.register_blueprint(main)

    return app
