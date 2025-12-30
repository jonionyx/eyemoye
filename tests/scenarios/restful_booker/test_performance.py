import pytest
from utils.validators import validate_json_schema
from schema.user_schema import USER_CREATE_SCHEMA

def test_booking_response_latency(api_client):
    """
    SLA Test:
    Create a booking to verify response is under 800ms

    """

    booking_data = {
        "firstname": "Performance",
        "lastname": "Tester",
        "totalprice": 100,
        "depositpaid": True,
        "bookingdates": {"checkin": "2025-01-01", "checkout": "2025-01-02"},
        "additionalneeds": "None"
    }

    response = api_client.post("/booking", json=booking_data)

    #  response.elapsed returns a timedelta object
    latency_ms = response.elapsed.total_seconds() * 1000

    print(f"\n Latency: {latency_ms: .2f}ms")

    assert latency_ms < 800, f"SLA Violation, response took {latency_ms}ms"