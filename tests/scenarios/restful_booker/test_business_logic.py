def test_business_logic_date_validation(api_client):
    payload = {
        "firstname": "Jim", "lastname": "Brown", "totalprice": 100, "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-12-01", 
            "checkout": "2025-01-01" # Checkout is 11 months BEFORE check-in
        }
    }
    response = api_client.post("/booking", json=payload)
    
    assert response.status_code == 400, "API allowed checkout date before checkin date!"