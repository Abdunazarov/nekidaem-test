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
async def test_read_news_feed(client):
    response = await client.get("/news_feed/user/1")
    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) <= 500
