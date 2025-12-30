import pytest
from utils.validators import validate_json_schema
from schema.user_schema import USER_CREATE_SCHEMA

# Define a list of tuples: (name, job, expected_status)
test_data = [
    ("John", "Engineer", 201),            # Standard case
    ("A", "Manager", 201),               # Boundary: Short name
    ("VeryLongNameExceedingNormalLimits", "Dev", 201), # Boundary: Long name
    ("", "Recruiter", 400),              # Negative: Empty name
    ("Alice", "", 400),                  # Negative: Empty job
]

@pytest.mark.parametrize("name, job, expected_status", test_data)
def test_create_user_data_driven(api_client, name, job, expected_status):
    """
    This test will run 5 times with the different inputs defined above.
    """
    payload = {"name": name, "job": job}
    response = api_client.post("/users", json=payload)
    
    assert response.status_code == expected_status
    
    # Only validate schema if we expect a successful creation
    if expected_status == 201:
        validate_json_schema(response.json(), USER_CREATE_SCHEMA)