from marshmallow import Schema, fields


class AlticciSequenceResponseSchema(Schema):
    term = fields.Int()
    value = fields.Int()
