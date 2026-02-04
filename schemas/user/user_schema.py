
      
from jsonschema import validate

USER_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "email": {"type": "string", "format": "email"},
        "phone": {"type": "string"},
        "firstName": {"type": "string"},
        "lastName": {"type": "string"},
        "kycStatus": {
            "type": "string",
            "enum": ["pending", "verified", "rejected"]
        },
        "createdAt": {"type": "string", "format": "date-time"},
        "updatedAt": {"type": "string", "format": "date-time"}
    },
    "required": ["id", "email", "firstName", "lastName", "kycStatus"],
    "additionalProperties": True
}

USERS_LIST_SCHEMA = {
    "type": "object",
    "required": ["data"],
    "properties": {
        "data": {
            "type": "array",
            "minItems": 1,
            "items": {
                "$ref": "#/definitions/user"
            }
        }
    },
    "definitions": {
        "user": {
            "type": "object",
            "required": [
                "id",
                "email",
                "firstName",
                "lastName",
                "updatedAt"
            ],
            "properties": {
                "id": {"type": "string"},
                "email": {"type": "string"},
                "phone": {"type": "string"},
                "firstName": {"type": "string"},
                "lastName": {"type": "string"},
                "kycStatus": {"type": "string"},
                "createdAt": {"type": "string", "format": "date-time"},
                "updatedAt": {"type": "string", "format": "date-time"}
            },
            "additionalProperties": False
        }
    }
}
