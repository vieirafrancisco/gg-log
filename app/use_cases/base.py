from typing import TypeVar

InputType = TypeVar('InputType')
OutputType = TypeVar('OutputType')


class UseCase[InputType, OutputType]:
    def execute(self, input_data: InputType) -> OutputType:
        raise NotImplementedError('Subclasses must implement this method')
