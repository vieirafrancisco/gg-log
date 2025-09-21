import pytest
from app.adapters.cryptography_jwt import CryptographyJWT
from app.config import Config

@pytest.fixture(autouse=True)
def set_jwt_secret():
    Config.JWT_SECRET_KEY = "test_secret"

@pytest.mark.parametrize("text", ["senha123", "outra_senha", "123456"])
def test_encode_and_decode(text):
    crypto = CryptographyJWT()
    encoded = crypto.encode(text)
    decoded = crypto.decode(encoded)
    assert decoded == text

def test_verify():
    crypto = CryptographyJWT()
    text = "verificar"
    encoded = crypto.encode(text)
    assert crypto.verify(text, encoded)
    assert not crypto.verify("errado", encoded)
