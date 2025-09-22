"""User repository module."""
from app.repositories.base import Repository
from app.models import User
from app.schemas.user import UserCreateInput, UserUpdateInput


class UserRepository(Repository[User, UserCreateInput, UserUpdateInput]):
    """
    Repository for managing User model.
    """
    def __init__(self):
        super().__init__(User)
