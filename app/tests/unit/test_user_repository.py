
import pytest
import pytest_asyncio
from tortoise import Tortoise
from app.models.user import User
from app.repositories.user import UserRepository
from app.schemas.user import UserCreateInput

@pytest_asyncio.fixture(scope="module", autouse=True)
async def init_db():
    await Tortoise.init(
        db_url="sqlite://:memory:",
        modules={"models": ["app.models.user"]}
    )
    await Tortoise.generate_schemas()
    yield
    await Tortoise.close_connections()

@pytest.mark.asyncio
async def test_create_and_get_user():
    repo = UserRepository()
    email = "test@repo.com"
    password_hash = "hash123"
    input_data = UserCreateInput(email=email, password_hash=password_hash)
    user = await repo.create(input_data)
    assert user.email == email
    assert user.password_hash == password_hash
    fetched = await repo.get_by_id(user.id)
    assert fetched.email == email

@pytest.mark.asyncio
async def test_delete_user():
    repo = UserRepository()
    email = "delete@repo.com"
    password_hash = "hash456"
    input_data = UserCreateInput(email=email, password_hash=password_hash)
    user = await repo.create(input_data)
    await repo.delete(user.id)
    fetched = await repo.get_by_id(user.id)
    assert fetched is None
