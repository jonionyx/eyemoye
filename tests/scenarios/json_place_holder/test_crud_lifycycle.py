import pytest
from utils.helpers import DataGenerator
import time

def test_post_lifecycle_crud(api_client):
    """
    Scenario: Create a post, vrify it exists, update it, ad delete it.
    Target API: https://jsonplaceholder.typicode.om/posts

    """
# Create (POST)
    payload = {
        "title": "Transformer Framework",
        "body": "CRUD Testing",
        "userId": 1
    }

    create_res = api_client.post("/posts", json=payload)
    assert create_res.status_code ==201
    post_id = create_res.json()["id"]

    # time.sleep(1)

    #  READ (GET)
    get_res = api_client.get(f"posts/{post_id}")
    assert get_res.status_code == 200
    assert get_res.json()["title"] == payload["title"]

    #  UPDATE (PUT)
    updated_payload = {
         "title": "Updated Title",
        "body": "Updated Body",
        "userId": 1

    }
    put_res = api_client.put(f"/posts/{post_id}", json=updated_payload)
    assert put_res.status_code == 200
    assert put_res.json()["title"] == "Updated Title"

    #  DELETE (DELETE)

    del_res = api_client.delete(f"/posts/{post_id}")
    assert del_res.status_code in [200, 204]




