from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_get_random_tip():
    response = client.get("/random_tip")
    assert response.status_code == 200
    assert "tip" in response.json()


def test_get_category_tip():
    response = client.get("/categorytip/packing")
    assert response.status_code == 200
    assert "tip" in response.json()


def test_get_category_tip_not_found():
    response = client.get("/categorytip/nonexistent")
    assert response.status_code == 404
    assert response.json() == {"detail": "Category not found"}
