from marshmallow import Schema, fields


class AlticciSequenceTermResponseSchema(Schema):
    term = fields.Int(required=True)
    value = fields.Int(required=True)
