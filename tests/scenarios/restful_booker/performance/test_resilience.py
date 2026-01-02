import requests
import pytest

def test_api_timeout_handling(api_client):
    """
    Scenario: If the server takes longer than the client's timeout, 
    the framework should raise a Timeout error gracefully.
    """
    # We use a public delay API to force a 5-second wait
    # Our client is configured with a shorter timeout (e.g., 2s)
    
    with pytest.raises(requests.exceptions.Timeout):
        # We manually override the timeout for this specific call to 1 second
        api_client.get("https://reqres.in/api/users?delay=5", timeout=1)
    
    print("\nResilience: Client correctly timed out on slow response.")