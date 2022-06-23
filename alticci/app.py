from flask import Flask

app = Flask(__name__)

from alticci.sequence.views import blueprint as sequence_bp

app.register_blueprint(sequence_bp)
