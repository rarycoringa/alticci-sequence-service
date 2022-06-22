from flask import Flask

from app.alticci.views import blueprint as alticci_bp
from app.hello.views import blueprint as hello_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(alticci_bp)
    app.register_blueprint(hello_bp)

    return app
