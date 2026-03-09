import pytest
from unittest.mock import patch

def test_data_isolation(client):
    # User 1 creates a task
    with patch("src.auth.middleware.verify_jwt") as mock_auth:
        mock_auth.return_value = {"sub": "user_1"}
        client.post(
            "/todos",
            json={"title": "User 1 Task"},
            headers={"Authorization": "Bearer token1"}
        )

    # User 2 tries to list tasks
    with patch("src.auth.middleware.verify_jwt") as mock_auth:
        mock_auth.return_value = {"sub": "user_2"}
        response = client.get("/todos", headers={"Authorization": "Bearer token2"})
        assert response.status_code == 200
        data = response.json()
        # Should NOT see user 1's task
        assert all(t["title"] != "User 1 Task" for t in data)

def test_prevent_cross_user_update(client):
    # User 1 creates a task
    with patch("src.auth.middleware.verify_jwt") as mock_auth:
        mock_auth.return_value = {"sub": "user_1"}
        res = client.post(
            "/todos",
            json={"title": "User 1 Task"},
            headers={"Authorization": "Bearer token1"}
        )
        todo_id = res.json()["id"]

    # User 2 tries to update User 1's task
    with patch("src.auth.middleware.verify_jwt") as mock_auth:
        mock_auth.return_value = {"sub": "user_2"}
        response = client.patch(
            f"/todos/{todo_id}",
            json={"title": "Hacked"},
            headers={"Authorization": "Bearer token2"}
        )
        # Should be 404 per TaskService implementation when not found for that user
        assert response.status_code == 404
