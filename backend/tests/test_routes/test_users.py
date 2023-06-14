import json


def test_create_user(client):
    data = {
        "name": "testuser",
        "email": "testuser@ornaman.com",
        "password": "testing",
        "id_rec": "tes-id_rec",
    }
    response = client.post("/users/", json=data)  # Pass the data dictionary directly
    # response = client.post("/users/",json.dumps(data)) ## this line output error
    assert response.status_code == 200
    assert response.json()["email"] == "testuser@ornaman.com"
    assert response.json()["is_active"] == True
