
USER_CREATE_SCHEMA = {
    "type": "object",
    "properties": {
        "lastname": {"type": "string"},
        "firstname": {"type": "string"},
        "job": {"type": "string"},
        "id": {"type": "string"},
        "createdAt": {"type": "string", "format": "date-time"}

    },
    "required": ["roles", "createdAt"],
    "additionalProperties": False

}
       
USER_CREATE_RESPONSE_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "number"}, # The database ID generated
        "firstname": {"type": "string", "minLength": 1},
        "lastname": {"type": "string", "minLength": 1},
        "email": {"type": "string", "format": "email"},
        "roles": {
            "type": "array",
            "items": {"type": "string"},
            "minItems": 0
        },
        "companyId": {"type": "integer"},
        "userId": {"type": "integer"},
        "createdAt": {"type": "string", "format": "date-time"}
    },
    "required": ["firstname", "email", "companyId", "userId"],
    "additionalProperties": False # Prevents undocumented data leakage
}