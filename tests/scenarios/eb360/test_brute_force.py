import time

def test_login_rate_limiting(api_client):
    """
    Scenario: Send 20 failed login attempts in 5 seconds.
    The API should eventually return 429 (Too Many Requests).
    """
    login_url = "api/authenticate/eb360"
    payload = {"username": "gjindal", "password": "Password1!"}
    
    status_codes = []
    for _ in range(20):
        response = api_client.post(login_url, json=payload)
        status_codes.append(response.status_code)
        
    # Check if the API triggered a 429 'Too Many Requests' at any point
    assert 429 in status_codes, "Security Gap: No rate limiting detected on login endpoint!"