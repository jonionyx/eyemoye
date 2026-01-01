import pytest
import allure
from faker import Faker

fake = Faker()
# fake.seed_instance(202601)

@allure.severity(allure.severity_level.CRITICAL)
def generate_unique_users(count=10):
    """Generates a list of unique user payloads."""
    users = []
    for _ in range(count):
        users.append({
            "firstname": fake.first_name(),
            "lastname": fake.last_name(),
            "email": fake.unique.email(),  # Guarantees unique email
            "roles": ["basic"],
            "companyId": 848, #fake.random_int(min=100, max=999),
            "userId": 7098 #fake.unique.random_int(min=1000, max=99999) # Unique ID
        })
    return users

@pytest.mark.parametrize("user_data", generate_unique_users(5))
def test_user_stress_creation(api_client, user_data):
    """
    Stress Test: Running 20 unique creations. 
    Faker ensures no 'Duplicate' errors occur.
    """
    with allure.step("Step 1: Send POST request to /user"):
         response = api_client.post("/api/add/platform/user", json=user_data)

    with allure.step("Step 2: Verify status code is 200"):
         assert response.status_code == 200


    with allure.step("Step 3:  Attach response to report"):
        # This allows you to see the actual JSON in the Allure report
        allure.attach(
            body=str(response.json()), 
            name="API_Response", 
            attachment_type=allure.attachment_type.JSON
            )