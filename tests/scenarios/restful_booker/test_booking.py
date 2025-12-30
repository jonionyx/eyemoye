from utils.helpers import DataGenerator
from utils.validators import validate_json_schema
from schema.user_schema import BOOKING_SCHEMA
import json

def test_create_booking_contract_validation(api_client):
    booking_data = {
        "firstname" : "Jim",
        "lastname" : "Brown",
        "totalprice" : 111,
        "depositpaid" : True,
        "bookingdates" : {
            "checkin" : "2018-01-01",
            "checkout" : "2019-01-01" 
               },
               "additionalneeds" : "Breakfast"
    }
    response = api_client.post("/booking", json=booking_data)
    # Check status code
    assert response.status_code == 200

    # JSON Printing
    response_data = response.json()
    pretty_json = json.dumps(response_data, indent=4)
    
    print(f"\n--- API RESPONSE DATA ---\n{pretty_json}")

    # Check the data structure (The Contract)
    validate_json_schema(response.json(), BOOKING_SCHEMA)