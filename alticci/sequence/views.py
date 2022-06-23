from flask import Blueprint, jsonify

from alticci.cache import cache
from alticci.sequence.controllers import retrieve_alticci_sequence_term

blueprint = Blueprint("alticci", __name__, url_prefix="/alticci")

@blueprint.route("/<int:term>", methods=["GET"])
@cache.cached(timeout=60, query_string=True)
def get_alticci_sequence_term(term):
    """
    """

    value = retrieve_alticci_sequence_term(term)

    response = {
        "term": term,
        "value": value,
    }

    status_code = 200

    return jsonify(response), status_code
