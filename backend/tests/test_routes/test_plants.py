# tests > test_routes > test_plants.py
# import json
from fastapi import status  # for deleting plant not use


def test_create_plant(
    client, normal_user_token_headers
):  # added normal_user_token_headers
    data = {
        "class_name": "Aglaonema",
        "family_name": "Araceae",
        "common_name": "Sri Rezeki",
        "taxonomic_data_url": "https://powo.science.kew.org/taxon/urn:lsid:ipni.org:names:2671-1",
        "location": "Indonesia",
        "description": "Aglaonema adalah tanaman hias populer dari suku talas-talasan atau Araceae. Genus Aglaonema memiliki sekitar 30 spesies. Mereka berasal dari daerah tropis dan subtropis di Asia dan Nugini. Mereka umumnya dikenal sebagai Chinese evergreens.",
        "date_posted": "2023-06-01",
    }

    # response = client.post("/plants/create-plant/",json.dumps(data)) #orror output TypeError: TestClient.post() takes 2 positional arguments but 3 were given
    # response = client.post("/plants/create-plant/", json=data)
    # response = client.post("/plants/create-plant/",data=json.dumps(data),headers=normal_user_token_headers)  # added header in the post request
    response = client.post(
        "/plants/create-plant/", json=data, headers=normal_user_token_headers
    )  # added header in the post request
    assert response.status_code == 200
    assert response.json()["family_name"] == "Araceae"
    assert (
        response.json()["description"]
        == "Aglaonema adalah tanaman hias populer dari suku talas-talasan atau Araceae. Genus Aglaonema memiliki sekitar 30 spesies. Mereka berasal dari daerah tropis dan subtropis di Asia dan Nugini. Mereka umumnya dikenal sebagai Chinese evergreens."
    )
    # Kita perlu memodifikasi setiap unit test di mana kita membuat request post/delete. Karena di sini tidak membatasi request get. Di sini tidak membutuhkan header untuk mendapatkan request.


def test_read_plant(
    client, normal_user_token_headers
):  # test read plant added normal_user_token_headers
    data = {
        "class_name": "Aglaonema",
        "family_name": "Araceae",
        "common_name": "Sri Rezeki",
        "taxonomic_data_url": "https://powo.science.kew.org/taxon/urn:lsid:ipni.org:names:2671-1",
        "location": "Indonesia",
        "description": "Aglaonema adalah tanaman hias populer dari suku talas-talasan atau Araceae. Genus Aglaonema memiliki sekitar 30 spesies. Mereka berasal dari daerah tropis dan subtropis di Asia dan Nugini. Mereka umumnya dikenal sebagai Chinese evergreens.",
        "date_posted": "2023-06-01",
    }

    # response = client.post("/plants/create-plant/",json.dumps(data)) ##TypeError: TestClient.post() takes 2 positional arguments but 3 were given
    # response = client.post("/plants/create-plant/", json=json.dumps(data))
    response = client.post(
        "/plants/create-plant/", json=data, headers=normal_user_token_headers
    )

    response = client.get("/plants/get/1/")
    assert response.status_code == 200
    assert response.json()["class_name"] == "Aglaonema"


# List data
def test_read_all_plants(
    client, normal_user_token_headers
):  # test read all plants added normal_user_token_headers
    data = {
        "class_name": "Aglaonema",
        "family_name": "Araceae",
        "common_name": "Sri Rezeki",
        "taxonomic_data_url": "https://powo.science.kew.org/taxon/urn:lsid:ipni.org:names:2671-1",
        "location": "Indonesia",
        "description": "Aglaonema adalah tanaman hias populer dari suku talas-talasan atau Araceae. Genus Aglaonema memiliki sekitar 30 spesies. Mereka berasal dari daerah tropis dan subtropis di Asia dan Nugini. Mereka umumnya dikenal sebagai Chinese evergreens.",
        "date_posted": "2023-06-01",
    }
    # client.post("/plants/create-plant/", json.dumps(data))
    # client.post("/plants/create-plant/", json.dumps(data))
    client.post("/plants/create-plant/", json=data, headers=normal_user_token_headers)
    client.post("/plants/create-plant/", json=data, headers=normal_user_token_headers)

    response = client.get("/plants/all/")
    assert response.status_code == 200
    assert response.json()[0]
    assert response.json()[1]


def test_update_a_plant(
    client, normal_user_token_headers
):  # test update a plant & added normal_user_token_headers
    data = {
        "class_name": "NEW Aglaonema",
        "family_name": "NEW Araceae",
        "common_name": "NEW Sri Rezeki",
        "taxonomic_data_url": "https://powo.science.kew.org/taxon/urn:lsid:ipni.org:names:2671-1",
        "location": "Indonesia",
        "description": "NEW Aglaonema adalah tanaman hias populer dari suku talas-talasan atau Araceae. Genus Aglaonema memiliki sekitar 30 spesies. Mereka berasal dari daerah tropis dan subtropis di Asia dan Nugini. Mereka umumnya dikenal sebagai Chinese evergreens.",
        "date_posted": "2023-06-01",
    }
    # json=json.dumps(data)
    # client.post("/plants/create-plant/",json.dumps(data))
    client.post("/plants/create-plant/", json=data, headers=normal_user_token_headers)
    data["class_name"] = "test NEW class_name"
    # response = client.put("/plants/update/1",json.dumps(data))
    response = client.put("/plants/update/1", json=data)
    assert response.json()["detail"] == "Successfully updated data."


def test_delete_a_plant(
    client, normal_user_token_headers
):  # test delete plant  & added normal_user_token_headers
    data = {
        "class_name": "NEW Aglaonema",
        "family_name": "NEW Araceae",
        "common_name": "NEW Sri Rezeki",
        "taxonomic_data_url": "https://powo.science.kew.org/taxon/urn:lsid:ipni.org:names:2671-1",
        "location": "Indonesia",
        "description": "NEW Aglaonema adalah tanaman hias populer dari suku talas-talasan atau Araceae. Genus Aglaonema memiliki sekitar 30 spesies. Mereka berasal dari daerah tropis dan subtropis di Asia dan Nugini. Mereka umumnya dikenal sebagai Chinese evergreens.",
        "date_posted": "2023-06-01",
    }
    # client.post("/plants/create-plant/",json.dumps(data))
    client.post("/plants/create-plant/", json=data, headers=normal_user_token_headers)
    # msg = client.delete("/plants/delete/1")
    client.delete("/plants/delete/1", headers=normal_user_token_headers)
    response = client.get("/plants/get/1/")
    assert response.status_code == status.HTTP_404_NOT_FOUND
