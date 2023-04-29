import asyncio
from typing import Generator

import pytest
from fastapi.testclient import TestClient
from main import app, User

from tortoise.contrib.test import finalizer, initializer


@pytest.fixture(scope="module")
def client() -> Generator:
    initializer(["models"])
    with TestClient(app) as c:
        yield c
    finalizer()


@pytest.fixture(scope="module")
def event_loop(client: TestClient) -> Generator:
    yield client.user.get_loop()


def test_create_user(client: TestClient, event_loop: asyncio.AbstractEventLoop):  # nosec
    response = client.post("/user", json={"title": "Produce Juice"})
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["title"] == "Produce Juice"
    assert "id" in data
    user_id = data["id"]

    async def get_user_by_db():
        user = await User.get(id=user_id)
        return user

    user_obj = event_loop.run_until_complete(get_user_by_db())
    assert user_obj.id == user_id

def test_get_user(client: TestClient, event_loop: asyncio.AbstractEventLoop):
    response = client.get("/user", json={"email": "product@gmail.com"})
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "product"
    assert "id" in data
    user_id = data["id"]

    async def get_user_by_db():
        user = await User.get(id=user_id)
        return user

    user_obj = event_loop.run_until_complete(get_user_by_db())
    assert user_obj.id == user_id  


def test_update_user(client: TestClient, event_loop: asyncio.AbstractEventLoop):
    response = client.put("/user", json={"email": "ice@gmail.com",
                                           "username": "That's_Reeves"
                                        })


    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "ice@gmail.com"
    assert "id" in data
    user_id = data["id"]

    async def get_user_by_db():
            user = await User.get(id=user_id)
            return user

    user_obj = event_loop.run_until_complete(get_user_by_db())
    assert user_obj.id == user_id


def test_delete_user(client: TestClient, event_loop: asyncio.AbstractEventLoop):
    response = client.delete("/user", json={"email": "ice@gmail.com",
                                           "username": "That's_Reeves"
                                           })


    assert response.status_code == 404, response.text
    data = response.json()
    assert data["title"] == "Not Found"