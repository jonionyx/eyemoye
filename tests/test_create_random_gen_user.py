from utils.helpers import DataGenerator
from utils.validators import validate_json_schema
from schema.user_schema import USER_CREATE_SCHEMA

def test_create_random_user(api_client):
    # Generate fresh user data for every test run
    payload = DataGenerator.generate_user_payload()

    response = api_client.post("/users", json=payload)
    assert response.status_code == 201

