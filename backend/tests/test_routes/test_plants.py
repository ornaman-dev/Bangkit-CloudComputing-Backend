import json


def test_create_plant(client):  # test create plant
    data = {
        "english_name": "Agglonema",
        "family_name": "Araceae",
        "common_name": "Sri Rezeki",
        "wikipedia_url": "id.wikipedia.org/wiki/Sri_rezeki",
        "location": "Indonesia",
        "description": "Agglonema adalah tanaman hias populer dari suku talas-talasan atau Araceae. Genus Aglaonema memiliki sekitar 30 spesies. Mereka berasal dari daerah tropis dan subtropis di Asia dan Nugini. Mereka umumnya dikenal sebagai Chinese evergreens.",
        "date_posted": "2023-06-01",
    }

    # response = client.post("/plants/create-plant/",json.dumps(data)) #orror output TypeError: TestClient.post() takes 2 positional arguments but 3 were given
    response = client.post("/plants/create-plant/", json=data)
    assert response.status_code == 200
    assert response.json()["family_name"] == "Araceae"
    assert (
        response.json()["description"]
        == "Agglonema adalah tanaman hias populer dari suku talas-talasan atau Araceae. Genus Aglaonema memiliki sekitar 30 spesies. Mereka berasal dari daerah tropis dan subtropis di Asia dan Nugini. Mereka umumnya dikenal sebagai Chinese evergreens."
    )


def test_read_plant(client):  # test read plant
    data = {
        "english_name": "Agglonema",
        "family_name": "Araceae",
        "common_name": "Sri Rezeki",
        "wikipedia_url": "id.wikipedia.org/wiki/Sri_rezeki",
        "location": "Indonesia",
        "description": "Agglonema adalah tanaman hias populer dari suku talas-talasan atau Araceae. Genus Aglaonema memiliki sekitar 30 spesies. Mereka berasal dari daerah tropis dan subtropis di Asia dan Nugini. Mereka umumnya dikenal sebagai Chinese evergreens.",
        "date_posted": "2023-06-01",
    }

    # response = client.post("/plants/create-plant/",json.dumps(data)) ##TypeError: TestClient.post() takes 2 positional arguments but 3 were given
    # response = client.post("/plants/create-plant/", json=json.dumps(data))
    response = client.post("/plants/create-plant/", json=data)

    response = client.get("/plants/get/1/")
    assert response.status_code == 200
    assert response.json()["english_name"] == "Agglonema"
