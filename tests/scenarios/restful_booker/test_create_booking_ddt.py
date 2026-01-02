import json
import pytest

def load_test_data(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

# Use @pytest.mark.parametrize to run the test once for each item in the JSON array
@pytest.mark.parametrize("booking", load_test_data("data/booking_payload.json"))
def test_create_booking_from_file(booking):
    print(f"Running test for: {booking['test_id']}")
    
    # Example assertion: Ensure the data was loaded correctly
    assert "firstname" in booking
    assert isinstance(booking["totalprice"], int)