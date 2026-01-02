import allure
import pytest

@allure.suite("Booking Management")
@allure.feature("Create Booking")
class TestBooking:

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("User can create a valid booking")
    @allure.description("This test verifies that a user can successfully create a booking and receives a 200 OK.")
    def test_create_booking_success(self, api_client):
        booking_data = {
            "firstname": "Allure",
            "lastname": "Report",
            "totalprice": 100,
            "depositpaid": True,
            "bookingdates": {"checkin": "2025-01-01", "checkout": "2025-01-02"},
            "additionalneeds": "Breakfast"
        }

        with allure.step("Step 1: Send POST request to /booking"):
            response = api_client.post("/booking", json=booking_data)
        
        with allure.step("Step 2: Verify status code is 200"):
            assert response.status_code == 200
            
        with allure.step("Step 3: Attach response to report"):
            # This allows you to see the actual JSON in the Allure report
            allure.attach(
                body=str(response.json()), 
                name="API_Response", 
                attachment_type=allure.attachment_type.JSON
            )