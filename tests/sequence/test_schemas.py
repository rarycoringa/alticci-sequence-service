import pytest

from alticci.sequence.schemas import AlticciSequenceTermResponseSchema


class TestAlticciSequenceResponseSchema:
    def test_schema(self):
        schema = AlticciSequenceTermResponseSchema()
        response = schema.dump(
            {
                "term": 6,
                "value": 3,
            }
        )

    def test_schema_str_types_to_int(self):
        schema = AlticciSequenceTermResponseSchema()
        response = schema.dump(
            {
                "term": "6",
                "value": "3",
            }
        )

    def test_schema_wrong_type(self):
        schema = AlticciSequenceTermResponseSchema()

        with pytest.raises(ValueError):
            response = schema.dump(
                {
                    "term": "string",
                    "value": 3,
                }
            )
