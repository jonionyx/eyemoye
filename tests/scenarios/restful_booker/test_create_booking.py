import json
import requests
from utils.validators import validate_json_schema
from schemas.booking.booking_schema import BOOKING_SCHEMA

def test_create_booking_id(api_client):
    """Fixture to create a temporary booking to test against."""

   
    payload = {
        "firstname": "QA_Senior",
        "lastname": "Test",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {"checkin": "2025-01-01", "checkout": "2025-01-02"}
    }
    response = api_client.post("/booking", json=payload)
    # Check status code
    assert "bookingid" in response.json()

    validate_json_schema(response.json(), BOOKING_SCHEMA)
   

