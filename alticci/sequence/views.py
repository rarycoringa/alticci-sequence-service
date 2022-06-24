from flask import jsonify
from flask_restful import Resource

from alticci.app import cache
from alticci.sequence.controllers import retrieve_alticci_sequence_term
from alticci.sequence.schemas import AlticciSequenceTermResponseSchema


class AlticciSequenceTermView(Resource):
    @cache.cached(timeout=60, query_string=True)
    def get(self, term: int):
        """
        Returns the calculated value of the requested term.
        ---
        tags:
            - Sequence
        parameters:
          - name: term
            description: A non-negative integer.
            in: path
            type: int
            required: true
        definitions:
            AlticciSequenceTermResponseSchema:
                type: object
                properties:
                    term:
                        type: int
                        example: 10
                    value:
                        type: int
                        example: 9
        responses:
            200:
                description: An object containing the requested term and the calculated value.
                schema:
                    $ref: '#/definitions/AlticciSequenceTermResponseSchema'
        """

        value = retrieve_alticci_sequence_term(term)

        schema = AlticciSequenceTermResponseSchema()
        response = schema.dump(
            {
                "term": term,
                "value": value,
            }
        )

        status_code = 200

        return response, status_code


class AlticciSequenceTermListView(Resource):
    @cache.cached(timeout=60, query_string=True)
    def get(self, first_term: int, last_term: int):
        """
        Returns the calculated value of the requested term.
        ---
        tags:
            - Sequence
        parameters:
          - name: first_term
            description: A non-negative integer less than or equal to "last_term".
            in: path
            type: int
            required: true
          - name: last_term
            description: A non-negative integer greater than or equal to "first_term".
            in: path
            type: int
            required: true
        definitions:
            AlticciSequenceTermResponseSchema:
                type: object
                properties:
                    term:
                        type: int
                        example: 10
                    value:
                        type: int
                        example: 9
            list:
                type: list[AlticciSequenceTermResponseSchema]
                example: [
                    {"term": 5, "value": 2},
                    {"term": 6, "value": 3},
                    {"term": 7, "value": 4},
                ]
        responses:
            200:
                description: A list containing the requested terms requested and the calculated values.
                schema:
                    $ref: '#/definitions/list'
        """

        try:
            assert last_term >= first_term
        except AssertionError:
            response = {
                "message": "The first term must be an integer less than or equal to the second term."
            }

            status_code = 400

            return response, status_code

        schema = AlticciSequenceTermResponseSchema()
        response = []

        for term in range(first_term, last_term + 1):
            value = retrieve_alticci_sequence_term(term)
            response.append(
                schema.dump(
                    {
                        "term": term,
                        "value": value,
                    }
                )
            )

        status_code = 200

        return response, status_code
