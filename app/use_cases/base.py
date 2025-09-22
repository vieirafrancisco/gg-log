"""Base use case class."""
from typing import TypeVar
from abc import ABC, abstractmethod

InputType = TypeVar('InputType')  # pylint: disable=invalid-name
OutputType = TypeVar('OutputType')  # pylint: disable=invalid-name


class UseCase[InputType, OutputType](ABC):  # pylint: disable=invalid-name
    """
    Base use case class.
    """
    @abstractmethod
    async def execute(self, input_data: InputType) -> OutputType:
        """
        Execute the use case with the given input data.
        """
