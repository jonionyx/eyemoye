import allure

def test_business_logic_date_validation(api_client):
    payload = {
        "firstname": "Jim", "lastname": "Brown", "totalprice": 100, "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-12-01", 
            "checkout": "2025-01-01" # Checkout is 11 months BEFORE check-in
        }
    }
    with allure.step("Step 1: Send POST request to /booking"):
           response = api_client.post("/booking", json=payload)
    
    with allure.step("Step 2: Verify status code is 400"):
           assert response.status_code == 400, "API allowed checkout date before checkin date!"

    with allure.step("Step 3: Attach response to report"):
            # This allows you to see the actual JSON in the Allure report
            allure.attach(
                body=str(response.json()), 
                name="API_Response", 
                attachment_type=allure.attachment_type.JSON
            )