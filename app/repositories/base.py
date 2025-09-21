from typing import TypeVar
from dataclasses import asdict

Model = TypeVar('Model')
ModelCreateInput = TypeVar('ModelCreateInput')
ModelUpdateInput = TypeVar('ModelUpdateInput')

class Repository[Model, ModelCreateInput, ModelUpdateInput]:
    def __init__(self, model: Model):
        self.model = model

    async def get_all(self):
        return await self.model.all()

    async def get_by_id(self, id: str):
        return await self.model.get_or_none(id=id)

    async def create(self, create_input: ModelCreateInput):
        return await self.model.create(**asdict(create_input))

    async def update(self, id: str, update_input: ModelUpdateInput):
        return await self.model.filter(id=id).update(**asdict(update_input))

    async def delete(self, id: str):
        instance = await self.model.get_or_none(id=id)
        await instance.delete()
