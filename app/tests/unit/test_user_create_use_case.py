import pytest
import asyncio
from unittest.mock import AsyncMock, MagicMock
from app.use_cases.user.user_create import UserCreateUseCase
from app.schemas.user import UserCreateUseCaseInput, UserCreateUseCaseOutput, UserCreateInput

@pytest.mark.asyncio
async def test_execute_creates_user():
    # Arrange
    mock_user = MagicMock()
    mock_user.email = "test@example.com"
    mock_user.id = 1
    mock_user.is_active = True
    mock_user.to_dict = lambda: {
        "email": mock_user.email,
        "id": mock_user.id,
        "is_active": mock_user.is_active
    }
    mock_user_repository = MagicMock()
    mock_user_repository.create = AsyncMock(return_value=mock_user)
    mock_cryptography_service = MagicMock()
    mock_cryptography_service.encode.return_value = "hashed_password"

    input_data = UserCreateUseCaseInput(email="test@example.com", password="plain_password")
    user_create_input = UserCreateInput(email="test@example.com", password_hash="hashed_password")

    use_case = UserCreateUseCase(mock_user_repository, mock_cryptography_service)

    # Act
    result = await use_case.execute(input_data)

    # Assert
    mock_cryptography_service.encode.assert_called_once_with("plain_password")
    mock_user_repository.create.assert_awaited_once_with(user_create_input)
    assert isinstance(result, UserCreateUseCaseOutput)
    assert result.email == "test@example.com"
    assert result.is_active == True
    assert result.id == 1
