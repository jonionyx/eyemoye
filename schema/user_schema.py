
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

BOOKING_SCHEMA = {
    "type": "object",
    "properties": {
        "firstname": {"type": "string"},
        "lastname": {"type": "string"},
        "totalprice": {"type": "number"}
    },
    "required": ["firstname", "lastname"]
}
       
