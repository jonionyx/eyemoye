def test_extremely_large_payload(api_client):
    """
    Scenario: Sending a firstname that is 100,000 characters long.
    """
    large_name = "A" * 100000
    payload = {
        "firstname": large_name,
        "lastname": "Tester",
        "totalprice": 10,
        "depositpaid": True,
        "bookingdates": {"checkin": "2025-01-01", "checkout": "2025-01-02"}
    }
    
    response = api_client.post("/booking", json=payload)
    
    # Many APIs have a 413 'Payload Too Large' limit
    assert response.status_code in [400, 413], f"API accepted a massive payload! Status: {response.status_code}"