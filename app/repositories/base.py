"""Generic repository for CRUD operations."""
from typing import TypeVar, Type
from dataclasses import asdict

from app.models.base import BaseModel

Model = TypeVar('Model', bound=BaseModel)
ModelCreateInput = TypeVar('ModelCreateInput')
ModelUpdateInput = TypeVar('ModelUpdateInput')


class Repository[Model, ModelCreateInput, ModelUpdateInput]:
    """
    Generic repository for CRUD operations.
    """
    def __init__(self, model: Type[Model]):
        self.model = model

    async def get_all(self):
        """Retrieve all instances of the model."""
        return await self.model.all()

    async def get_by_id(self, id: str):  # pylint: disable=redefined-builtin
        """Retrieve a single instance of the model by ID."""
        return await self.model.get_or_none(id=id)

    async def create(self, create_input: ModelCreateInput):
        """Create a new instance of the model."""
        return await self.model.create(**asdict(create_input))

    async def update(self, id: str, update_input: ModelUpdateInput):  # pylint: disable=redefined-builtin
        """Update an existing instance of the model."""
        return await self.model.filter(id=id).update(**asdict(update_input))

    async def delete(self, id: str):  # pylint: disable=redefined-builtin
        """Delete an instance of the model by ID."""
        instance = await self.model.get_or_none(id=id)
        if instance:
            await instance.delete()
