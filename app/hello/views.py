from flask import Blueprint, jsonify


blueprint = Blueprint("hello", __name__, url_prefix="/hello")


@blueprint.route("/", methods=["GET"])
def hello():
    message = {"message": "Hello world!"}

    return jsonify(message), 200
