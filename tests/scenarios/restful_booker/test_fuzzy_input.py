import requests

def test_fuzz_input():
    url = "https://restful-booker.herokuapp.com/booking"
    # Sending a string "expensive" instead of an integer for totalprice
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": "expensive", 
        "depositpaid": True,
        "bookingdates": {"checkin": "2023-01-01", "checkout": "2023-01-02"}
    }

   
    response = requests.post(url, json=payload)
    
     
    # We expect a 400 Bad Request, NOT a 500 Internal Server Error
    if response.status_code == 500:
        print("FAIL: Server crashed (500) due to unhandled input type.")
    else:
        print(f"Server handled bad input with status: {response.status_code}")

test_fuzz_input()