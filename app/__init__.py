from flask import Flask

from app.hello.views import blueprint as hello_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(hello_bp)

    return app
