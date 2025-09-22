import pytest
from app.use_cases.base import UseCase

class DummyInput:
    pass

class DummyOutput:
    pass

class DummyUseCase(UseCase[DummyInput, DummyOutput]):
    async def execute(self, input_data: DummyInput) -> DummyOutput:
        return DummyOutput()

@pytest.mark.asyncio
async def test_dummy_use_case():
    use_case = DummyUseCase()
    result = await use_case.execute(DummyInput())
    assert isinstance(result, DummyOutput)
