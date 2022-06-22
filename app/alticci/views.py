from flask import Blueprint, jsonify

from app.alticci.controllers import retrieve_alticci_term

blueprint = Blueprint("alticci", __name__, url_prefix="/alticci")

@blueprint.route("/<int:term>", methods=["GET"])
def get_alticci_term(term):
    value = retrieve_alticci_term(term)

    response = {
        "term": term,
        "value": value,
    }

    status_code = 200

    return jsonify(response), status_code
