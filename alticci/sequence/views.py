from flask import jsonify
from flask.views import MethodView

from alticci.app import cache
from alticci.sequence.controllers import retrieve_alticci_sequence_term
from alticci.sequence.schemas import AlticciSequenceResponseSchema


class AlticciSequenceTermView(MethodView):
    @cache.cached(timeout=60, query_string=True)
    def get(self, term):
        """
        """

        value = retrieve_alticci_sequence_term(term)

        schema = AlticciSequenceResponseSchema()
        response = schema.dump(
            {
                "term": term,
                "value": value,
            }
        )

        status_code = 200

        return jsonify(response), status_code
