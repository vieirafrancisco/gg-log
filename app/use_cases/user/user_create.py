from app.use_cases.base import UseCase
from app.repositories.user import UserRepository
from app.ports.cryptography import Cryptography
from app.schemas.user import UserCreateUseCaseInput, UserCreateUseCaseOutput, UserCreateInput


class UserCreateUseCase(UseCase[UserCreateUseCaseInput, UserCreateUseCaseOutput]):
    def __init__(self, user_repository: UserRepository, crypthography_service: Cryptography):
        self.user_repository = user_repository
        self.crypthography_service = crypthography_service

    async def execute(self, input_data: UserCreateUseCaseInput) -> UserCreateUseCaseOutput:
        user_create_input = UserCreateInput(
            email=input_data.email,
            password_hash=self.crypthography_service.encode(input_data.password)
        )
        user = await self.user_repository.create(user_create_input)
        return UserCreateUseCaseOutput(
            id=user.id,
            email=user.email,
            is_active=user.is_active
        )
