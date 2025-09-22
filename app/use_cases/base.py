"""Base use case class."""
from typing import TypeVar
from abc import ABC, abstractmethod

from pydantic import BaseModel as PydanticBaseModel

InputType = TypeVar('InputType', bound=PydanticBaseModel)  # pylint: disable=invalid-name
OutputType = TypeVar('OutputType', bound=PydanticBaseModel)  # pylint: disable=invalid-name


class UseCase[InputType, OutputType](ABC):  # pylint: disable=invalid-name
    """
    Base use case class.
    """
    @abstractmethod
    async def execute(self, input_data: InputType) -> OutputType:
        """
        Execute the use case with the given input data.
        """
