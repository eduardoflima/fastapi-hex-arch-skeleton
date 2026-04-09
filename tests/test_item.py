from fastapi.testclient import TestClient
from src.main import app
from src.adapters.inbound.api.schemas import ItemResponse

client = TestClient(app)


def test_retrieve_items():
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == [ItemResponse(id=1, name="some item").model_dump()]


def test_retrieve_item():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == ItemResponse(id=1, name="some item").model_dump()


def test_create_item():
    response = client.post("/items", json={ "name": "some item" })
    assert response.status_code == 201
    assert response.json() == ItemResponse(id=2, name="some item").model_dump()


def test_update_item():
    response = client.put("/items/1", json={ "id": 1, "name": "some item changed" })
    assert response.status_code == 200
    assert response.json() == ItemResponse(id=1, name="some item changed").model_dump()

def test_delete_item():
    response = client.delete("/items/1")
    assert response.status_code == 204
