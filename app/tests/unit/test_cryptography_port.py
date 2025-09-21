import pytest
from app.ports.cryptography import Cryptography

class DummyCrypto(Cryptography):
    def encode(self, text: str) -> str:
        return text[::-1]
    def decode(self, encoded_text: str) -> str:
        return encoded_text[::-1]
    def verify(self, text: str, encoded_text: str) -> bool:
        return text == self.decode(encoded_text)

def test_cryptography_port_not_implemented():
    class IncompleteCrypto(Cryptography):
        pass
    with pytest.raises(TypeError):
        IncompleteCrypto()

def test_dummy_crypto():
    crypto = DummyCrypto()
    text = "abc123"
    encoded = crypto.encode(text)
    assert encoded == "321cba"
    decoded = crypto.decode(encoded)
    assert decoded == text
    assert crypto.verify(text, encoded)
    assert not crypto.verify("errado", encoded)
