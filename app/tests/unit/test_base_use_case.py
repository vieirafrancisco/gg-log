import pytest
from app.use_cases.base import UseCase

class DummyInput:
    pass

class DummyOutput:
    pass

class DummyUseCase(UseCase[DummyInput, DummyOutput]):
    def execute(self, input_data: DummyInput) -> DummyOutput:
        return DummyOutput()

def test_base_use_case_not_implemented():
    use_case = UseCase()
    with pytest.raises(NotImplementedError):
        use_case.execute(DummyInput())

def test_dummy_use_case():
    use_case = DummyUseCase()
    result = use_case.execute(DummyInput())
    assert isinstance(result, DummyOutput)
