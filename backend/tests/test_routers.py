from fastapi.testclient import TestClient
from main import app


def test_auth_register_stub():
    with TestClient(app) as client:
        response = client.post("/auth/register", json={"email": "a@b.com", "password": "12345678"})
        assert response.status_code == 200
        assert response.json() == {"message": "Not implemented"}


def test_auth_login_stub():
    with TestClient(app) as client:
        response = client.post("/auth/login", json={"email": "a@b.com", "password": "12345678"})
        assert response.status_code == 200
        assert response.json() == {"message": "Not implemented"}


def test_list_boards_stub():
    with TestClient(app) as client:
        response = client.get("/api/boards")
        assert response.status_code == 200
        assert response.json() == {"message": "Not implemented"}


def test_create_board_stub():
    with TestClient(app) as client:
        response = client.post("/api/boards", json={"title": "Test"})
        assert response.status_code == 200
        assert response.json() == {"message": "Not implemented"}


def test_list_cards_stub():
    with TestClient(app) as client:
        response = client.get("/api/boards/1/cards")
        assert response.status_code == 200
        assert response.json() == {"message": "Not implemented"}


def test_create_card_stub():
    with TestClient(app) as client:
        response = client.post("/api/boards/1/cards", json={"title": "Task"})
        assert response.status_code == 200
        assert response.json() == {"message": "Not implemented"}


def test_update_card_stub():
    with TestClient(app) as client:
        response = client.put("/api/cards/1", json={"title": "Updated"})
        assert response.status_code == 200
        assert response.json() == {"message": "Not implemented"}


def test_delete_card_stub():
    with TestClient(app) as client:
        response = client.delete("/api/cards/1")
        assert response.status_code == 200
        assert response.json() == {"message": "Not implemented"}


def test_update_card_status_stub():
    with TestClient(app) as client:
        response = client.patch("/api/cards/1/status", json={"status": "done"})
        assert response.status_code == 200
        assert response.json() == {"message": "Not implemented"}
