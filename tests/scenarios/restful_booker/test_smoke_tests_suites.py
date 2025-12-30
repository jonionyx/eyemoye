import pytest

def test_smoke_auth_and_connection(api_client):
    """
    Verify:
    1. .env credentials are loaded.
    2. Authentication endpoint /api/authenticate/eb360 works.
    3. The authToken is extracted and injected into headers.
    4. A follow-up GET request to a protected endpoint succeeds.
    """
    # Verify the client has an Authorization header (injected during setup)
    auth_header = api_client.session.headers.get("Authorization")
    assert auth_header is not None, "Authorization header is missing!"
    assert auth_header.startswith("Bearer "), "Authorization header is not a Bearer token!"

    # Perform a 'Who Am I' or Profile call to verify the token is valid
    # Replace '/api/user/profile' with a real lightweight endpoint from your API
    response = api_client.get("ping")
    
    assert response.status_code == 201, f"Smoke test failed! Status: {response.status_code}"
    # assert "OK" in response.text, "Response body did not contain expected user data"

    print("\n✅ Smoke Test Passed: Connection and Authentication are stable.")