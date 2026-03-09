import pytest
from unittest.mock import patch

@pytest.fixture
def mock_auth():
    with patch("src.auth.middleware.verify_jwt") as mock:
        mock.return_value = {"sub": "user_123"}
        yield mock

def test_create_task(client, mock_auth):
    response = client.post(
        "/todos",
        json={"title": "Test Task", "description": "This is a test"},
        headers={"Authorization": "Bearer valid_token"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Task"
    assert data["user_id"] == "user_123"

def test_list_tasks(client, mock_auth):
    # Create a task first
    client.post(
        "/todos",
        json={"title": "Task 1"},
        headers={"Authorization": "Bearer valid_token"}
    )
    
    response = client.get("/todos", headers={"Authorization": "Bearer valid_token"})
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1
    assert data[0]["title"] == "Task 1"

def test_update_task(client, mock_auth):
    res = client.post(
        "/todos",
        json={"title": "Old Title"},
        headers={"Authorization": "Bearer valid_token"}
    )
    todo_id = res.json()["id"]
    
    response = client.patch(
        f"/todos/{todo_id}",
        json={"title": "New Title", "completed": True},
        headers={"Authorization": "Bearer valid_token"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "New Title"
    assert data["completed"] is True

def test_delete_task(client, mock_auth):
    res = client.post(
        "/todos",
        json={"title": "To be deleted"},
        headers={"Authorization": "Bearer valid_token"}
    )
    todo_id = res.json()["id"]
    
    response = client.delete(f"/todos/{todo_id}", headers={"Authorization": "Bearer valid_token"})
    assert response.status_code == 204
    
    # Verify it's gone
    get_res = client.get("/todos", headers={"Authorization": "Bearer valid_token"})
    assert all(t["id"] != todo_id for t in get_res.json())

def test_unauthorized_access(client):
    response = client.get("/todos")
    assert response.status_code == 401
