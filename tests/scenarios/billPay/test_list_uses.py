from utils.validators import validate_json_schema
from jsonschema import validate
from schemas.user.user_schema import USERS_LIST_SCHEMA
import json
import requests

def validate_users_schema(users: list) -> None:
    for user in users:
        validate(instance=user, schema=USER_SCHEMA)



def test_get_users_list(api_client):
    """
    Retrieve list of users on platforms
    """
    
    response = api_client.get("/v1/users?page=1&limit=10")

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    validate_json_schema(response.json(), USERS_LIST_SCHEMA)

    res_body = response.json()
     
   
     
   
    # Assert wrapper structure
    assert "data" in res_body, "Missing 'data' key in response"
    assert isinstance(res_body["data"], list), "'data' should be a list"
    assert len(res_body["data"]) > 0, "'data' list is empty"
    # validate_json_schema(res_body, USER_SCHEMA)

    users = res_body["data"]
    
    # Assert required keys exist in each user object
    required_keys = {"id", "email", "firstName", "lastName", "updatedAt"}

    for user in users:
        assert isinstance(user, dict), "User item is not an object"
        missing = required_keys  - user.keys()
        assert not missing, f"Missing keys {missing} in user object"      
        json.dumps(users, indent=4, sort_keys=True)
       
       
    return users

 

# validate(instance=user, schema=USER_SCHEMA)
   
# from utils.validators import validate_json_schema
# from schemas.user.user_schema import USER_CREATE_SCHEMA



#  with allure.step(f"Executing test: {test_name}"):
#         response = api_client.post("/api/add/platform/user", json=full_payload)


#     with allure.step(f"Asserting status code is {expected_status}"):
#         assert response.status_code == expected_status, (
#             f"Failed {test_name}. Expected {expected_status} but got {response.status_code}. "
#             f"Response: {response.text}"
#         )

#     if response.status_code == 200:
#         with allure.step("Validating response schema"):
#             validate(instance=response.json(), schema=USER_CREATE_RESPONSE_SCHEMA)  