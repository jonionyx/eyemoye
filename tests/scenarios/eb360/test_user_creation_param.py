import pytest
import allure
from jsonschema import validate
from schemas.user.user_schema import USER_CREATE_RESPONSE_SCHEMA
from faker import Faker
fake = Faker()

#  Define the baseline "Happy Path" data
BASE_USER = {
    "firstname": fake.first_name(),
    "lastname": fake.last_name(),
    "email": fake.email(),
    "roles": ["basic", "admin"],
    "companyId": 848,
    "userId": 7098

}

@allure.suite("User Management")
@allure.feature("User Creation")
@pytest.mark.parametrize("test_name, payload_patch, expected_status",[
    ("Valid User Creation", {}, 200),
    # ("Empty Roles List", {"roles": []}, 200) # Check if roles are optional
    # ("Multiple Roles", {"roles": ["basic", "admin", "manager", "guest"]}, 200)
    ("Missing Email", {"email": None}, 400),
    ("Invalid Email Format", {"email": "not-an-email"}, 400),
    ("Large ID Boundary", {"companyId": 999999}, 201),
    ("Negative User ID", {"userId": -1}, 403),
    ("Non-existent Company", {"companyId": 0}, 400),
    ("SQL Injection Attempt", {"firstname": "'; DROP TABLE users;--"}, 400)


    ])
def test_create_user_permutations(api_client, test_name, payload_patch, expected_status):
    allure.dynamic.title(f"Permutation: {test_name}")

    # Create the actual payload by updating the base with the patch
    full_payload = BASE_USER.copy()
    full_payload.update(payload_patch)

    with allure.step(f"Executing test: {test_name}"):
        response = api_client.post("/api/add/platform/user", json=full_payload)


    with allure.step(f"Asserting status code is {expected_status}"):
        assert response.status_code == expected_status, (
            f"Failed {test_name}. Expected {expected_status} but got {response.status_code}. "
            f"Response: {response.text}"
        )

    if response.status_code == 200:
        with allure.step("Validating response schema"):
            validate(instance=response.json(), schema=USER_CREATE_RESPONSE_SCHEMA)    






