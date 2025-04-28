from marshmallow import Schema, fields, validates, ValidationError


class LoginSchema(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True, load_only=True)

    @validates('password')
    def validate_password(self, value):
        if len(value) < 6:
            raise ValidationError("Password must be at least 6 characters long")


class TokenSchema(Schema):
    access_token = fields.Str(required=True)
