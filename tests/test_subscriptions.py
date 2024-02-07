# thirdparty
import pytest
from httpx import AsyncClient
from main import app

# project


@pytest.fixture
async def client():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        yield ac


@pytest.mark.asyncio
async def test_subscribe(client):
    response = await client.post("/subscriptions/", json={"user_id": 1, "blog_id": 1})
    assert response.status_code == 200
    assert response.json()["user_id"] == 1
    assert response.json()["blog_id"] == 1


@pytest.mark.asyncio
async def test_unsubscribe(client):
    response = await client.delete("/subscriptions/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1


@pytest.mark.asyncio
async def test_read_subscriptions_for_user(client):
    response = await client.get("/subscriptions/user/1")
    assert response.status_code == 200
    assert type(response.json()) == list


@pytest.mark.asyncio
async def test_read_subscribers_for_blog(client):
    response = await client.get("/subscriptions/blog/1")
    assert response.status_code == 200
    assert type(response.json()) == list
