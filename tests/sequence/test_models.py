import pytest

from alticci.sequence.schemas import AlticciSequenceResponseSchema


class TestAlticciSequenceResponseSchema:
    def test_schema(self):
        schema = AlticciSequenceResponseSchema()
        response = schema.dump(
            {
                "term": 6,
                "value": 3,
            }
        )

    def test_schema_str_types_to_int(self):
        schema = AlticciSequenceResponseSchema()
        response = schema.dump(
            {
                "term": "6",
                "value": "3",
            }
        )

    def test_schema_wrong_type(self):
        schema = AlticciSequenceResponseSchema()

        with pytest.raises(ValueError):
            response = schema.dump(
                {
                    "term": "string",
                    "value": 3,
                }
            )
