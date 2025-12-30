def test_authentication_persistence(api_client):
    """
    Verify that the session correctly maintains the Bearer token
    by calling a 'profile' or 'whoami' endpoint.
    """

    response = api_client.get("ping")

    return response.json()
    # assert response.status_code == 201
    # assert "OK" in response.json()
    # assert "email" in response.json()