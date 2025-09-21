from abc import ABC, abstractmethod


class Cryptography(ABC):
    @abstractmethod
    def encode(self, text: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def decode(self, encoded_text: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def verify(self, text: str, encoded_text: str) -> bool:
        raise NotImplementedError
