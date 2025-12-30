import json
import requests
def test_get_users_list(api_client):
    """
    Retrievelist of users on platforms
    """
    payload = {
        "filter": "",
        "sort": "name|desc",
        "per_page": 50,
        "page": 1,
        "is_active": 0,
        "companyId": 804,
        "userId": 7098
    }
    response = api_client.post("api/platform/users/list", json=payload)
    # Check status code

    assert response.status_code == 200
    res_dict = response.json()
    print(json.dumps(res_dict, indent=4, sort_keys=True))
    # user_list = response.json()
   
   
    # for key in user_list: {
    #     print(key,":", user_list[key])
    # }

    