from utils.helpers import DataGenerator
from utils.validators import validate_json_schema
from schema.user_schema import USER_CREATE_SCHEMA

def test_create_random_user(api_client):
    # Generate fresh user data for every test run
    payload = DataGenerator. generate_placeholder_user()

    response = api_client.post("/users", json=payload)
    assert response.status_code == 201
    user_id = response.json()["id"]
    # assert response.json()["id"] == payload["id"]


     #  READ (GET)
    # get_res = api_client.get(f"users/{user_id}")
    # assert get_res.status_code == 200
    # assert get_res.json()["title"] == payload["title"]

def test_retrieve_user(api_client):
     get_res = api_client.get(f"users/{10}")
     assert get_res.status_code == 200
     assert get_res.json()["name"] == "Clementina DuBuque"
