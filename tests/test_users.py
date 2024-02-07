# thirdparty
import pytest
from httpx import AsyncClient

# project
from main import app


@pytest.fixture
async def client():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        yield ac


@pytest.mark.asyncio
async def test_create_user(client):
    user_data = {"username": "testuser", "email": "test@example.com", "name": "Test User"}
    response = await client.post("/users/", json=user_data)
    assert response.status_code == 200
    assert response.json()["username"] == user_data["username"]
    assert response.json()["email"] == user_data["email"]


@pytest.mark.asyncio
async def test_read_all_users(client):
    response = await client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
