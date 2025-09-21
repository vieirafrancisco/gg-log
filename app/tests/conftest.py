import os
import pytest

@pytest.fixture(scope="session", autouse=True)
def set_sqlite_memory_db():
    os.environ["DATABASE_URL"] = "sqlite://:memory:"
    yield
    # O banco em memória é destruído automaticamente ao final da sessão
