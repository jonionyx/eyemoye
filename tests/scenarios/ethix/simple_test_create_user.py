from utils.validators import validate_json_schema
from schema.user_schema import USER_CREATE_SCHEMA
import json

def test_create_user_success(api_client):
    """
    Test creating a new user using a POST request.
    The 'api_client' is automatically authenticated.
    """

    user_data = {
        "firstname": "Task",
        "lastname": "Initiator",
        "email": "initiator@yopmail.com",
        "roles": ["basic", "admin"],
        "companyId": 804,       
        "userId": 7098
    }

    response = api_client.post("/api/add/platform/user", json=user_data)

    #  Assertions
    assert response.status_code == 200
    result = response.json()
    for i in result: {
        print(json.dumps(i, indent=4, sort_keys=True))
    }
   


     # Check the data structure (The Contract)
    # validate_json_schema(response.json(), USER_CREATE_SCHEMA)
    