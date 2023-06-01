# tests > test_routes > test_plants.py
import json
from fastapi import status # for deleting plant not use


def test_create_plant(client):  # test create plant
    data = {
        "english_name": "Aglaonema",
        "family_name": "Araceae",
        "common_name": "Sri Rezeki",
        "wikipedia_url": "id.wikipedia.org/wiki/Sri_rezeki",
        "location": "Indonesia",
        "description": "Aglaonema adalah tanaman hias populer dari suku talas-talasan atau Araceae. Genus Aglaonema memiliki sekitar 30 spesies. Mereka berasal dari daerah tropis dan subtropis di Asia dan Nugini. Mereka umumnya dikenal sebagai Chinese evergreens.",
        "date_posted": "2023-06-01",
    }

    # response = client.post("/plants/create-plant/",json.dumps(data)) #orror output TypeError: TestClient.post() takes 2 positional arguments but 3 were given
    response = client.post("/plants/create-plant/", json=data)
    assert response.status_code == 200
    assert response.json()["family_name"] == "Araceae"
    assert (
        response.json()["description"]
        == "Aglaonema adalah tanaman hias populer dari suku talas-talasan atau Araceae. Genus Aglaonema memiliki sekitar 30 spesies. Mereka berasal dari daerah tropis dan subtropis di Asia dan Nugini. Mereka umumnya dikenal sebagai Chinese evergreens."
    )


def test_read_plant(client):  # test read plant
    data = {
        "english_name": "Aglaonema",
        "family_name": "Araceae",
        "common_name": "Sri Rezeki",
        "wikipedia_url": "id.wikipedia.org/wiki/Sri_rezeki",
        "location": "Indonesia",
        "description": "Aglaonema adalah tanaman hias populer dari suku talas-talasan atau Araceae. Genus Aglaonema memiliki sekitar 30 spesies. Mereka berasal dari daerah tropis dan subtropis di Asia dan Nugini. Mereka umumnya dikenal sebagai Chinese evergreens.",
        "date_posted": "2023-06-01",
    }

    # response = client.post("/plants/create-plant/",json.dumps(data)) ##TypeError: TestClient.post() takes 2 positional arguments but 3 were given
    # response = client.post("/plants/create-plant/", json=json.dumps(data))
    response = client.post("/plants/create-plant/", json=data)

    response = client.get("/plants/get/1/")
    assert response.status_code == 200
    assert response.json()["english_name"] == "Aglaonema"


# List data
def test_read_all_plants(client):
    data = {
        "english_name": "Aglaonema",
        "family_name": "Araceae",
        "common_name": "Sri Rezeki",
        "wikipedia_url": "id.wikipedia.org/wiki/Sri_rezeki",
        "location": "Indonesia",
        "description": "Aglaonema adalah tanaman hias populer dari suku talas-talasan atau Araceae. Genus Aglaonema memiliki sekitar 30 spesies. Mereka berasal dari daerah tropis dan subtropis di Asia dan Nugini. Mereka umumnya dikenal sebagai Chinese evergreens.",
        "date_posted": "2023-06-01",
    }
    # client.post("/plants/create-plant/", json.dumps(data))
    # client.post("/plants/create-plant/", json.dumps(data))
    client.post("/plants/create-plant/", json=data)
    client.post("/plants/create-plant/", json=data)

    response = client.get("/plants/all/")
    assert response.status_code == 200
    assert response.json()[0]
    assert response.json()[1]


def test_update_a_plant(client):
    data = {
        "english_name": "NEW Aglaonema",
        "family_name": "NEW Araceae",
        "common_name": "NEW Sri Rezeki",
        "wikipedia_url": "id.wikipedia.org/wiki/Sri_rezeki",
        "location": "Indonesia",
        "description": "NEW Aglaonema adalah tanaman hias populer dari suku talas-talasan atau Araceae. Genus Aglaonema memiliki sekitar 30 spesies. Mereka berasal dari daerah tropis dan subtropis di Asia dan Nugini. Mereka umumnya dikenal sebagai Chinese evergreens.",
        "date_posted": "2023-06-01",
    }
    # json=json.dumps(data)
    # client.post("/plants/create-plant/",json.dumps(data))
    client.post("/plants/create-plant/", json=data)
    data["english_name"] = "test NEW english_name"
    # response = client.put("/plants/update/1",json.dumps(data))
    response = client.put("/plants/update/1", json=data)
    assert response.json()["msg"] == "Successfully updated data."

def test_delete_a_plant(client):            #new
    data = {
        "english_name": "NEW Aglaonema",
        "family_name": "NEW Araceae",
        "common_name": "NEW Sri Rezeki",
        "wikipedia_url": "id.wikipedia.org/wiki/Sri_rezeki",
        "location": "Indonesia",
        "description": "NEW Aglaonema adalah tanaman hias populer dari suku talas-talasan atau Araceae. Genus Aglaonema memiliki sekitar 30 spesies. Mereka berasal dari daerah tropis dan subtropis di Asia dan Nugini. Mereka umumnya dikenal sebagai Chinese evergreens.",
        "date_posted": "2023-06-01",
    }
    # client.post("/plants/create-plant/",json.dumps(data))
    client.post("/plants/create-plant/",json=data)
    msg = client.delete("/plants/delete/1")
    response = client.get("/plants/get/1/")
    assert response.status_code == status.HTTP_404_NOT_FOUND
