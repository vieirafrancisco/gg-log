import jwt

from app.ports.cryptography import Cryptography
from app.config import Config


class CryptographyJWT(Cryptography):
    def encode(self, text: str) -> str:
        return jwt.encode(
            {'text': text}, Config.JWT_SECRET_KEY, algorithm='HS256'
        )

    def decode(self, encoded_text: str) -> str:
        decoded = jwt.decode(encoded_text, Config.JWT_SECRET_KEY, algorithms=['HS256'])
        return decoded['text']

    def verify(self, text: str, encoded_text: str) -> bool:
        return text == self.decode(encoded_text)