import pytest

@pytest.mark.parametrize("invalid_field, payload", 
                         [
                             ("string_instead_of_int", {"totalprice": "one hundred"}),
                             ("missing_required_field", {"lastname": "Brown"}), # Missing firstname
                             ("invalid_date_format", {"bookingdates": {"checkin": "01-01-2025"}}) # Wrong format
                        ]
                        )
def test_booking_invalid_data_types(api_client, invalid_field, payload):
    """
    Scenario: Sending malformed data types should return 400 Bad Request.
    """
    # We merge our bad data into a valid base structure
    base_booking = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {"checkin": "2025-01-01", "checkout": "2025-01-02"}
    }
    base_booking.update(payload)
    
    response = api_client.post("/booking", json=base_booking)
    
    # Expectation: 400 or 422, NEVER 500
    assert response.status_code in [400, 422, 415], f"Failed on {invalid_field}: {response.text}"