from app.repositories.base import Repository
from app.models import User
from app.schemas.user import UserCreateInput, UserUpdateInput


class UserRepository(Repository[User, UserCreateInput, UserUpdateInput]):
    def __init__(self):
        super(UserRepository, self).__init__(User)
