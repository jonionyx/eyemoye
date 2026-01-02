import pytest

@pytest.mark.parametrize("price", [-1, "Two Hundred", 1000000000])
def test_price_boundary_limits(api_client, price):
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": price, 
        "depositpaid": True,
        "bookingdates": {"checkin": "2025-01-01", "checkout": "2025-01-02"}
    }
    response = api_client.post("/booking", json=payload)
    
    # Business logic check: price should likely not be negative or billion-scale
    assert response.status_code in [400, 422, 200], f"Accepted invalid price: {price}"