from utils.helpers import DataGenerator
from utils.validators import validate_json_schema
from schemas.user.user_schema import USER_CREATE_SCHEMA

def test_delete_user_workflow(user_context, api_client):
    #  Setup: create a User vis fixture 
    payload = DataGenerator.generate_restfulbooker_user_payload()
    response = user_context(payload)
    user_id = response.json()["id"]

    # Action: Perform a GET request to verify existence
    get_res = api_client.get(f"/users/{user_id}")
    assert get_res.status_code == 200

    # Teardown happens automatically
