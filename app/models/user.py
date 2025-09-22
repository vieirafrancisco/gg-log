"""User model definition."""
from tortoise import fields

from app.models.base import BaseModel


class User(BaseModel):
    """
    User model.
    """
    email = fields.CharField(max_length=100, unique=True)
    password_hash = fields.CharField(max_length=128)
    is_active = fields.BooleanField(default=True)

    class Meta:  # pylint: disable=missing-class-docstring
        table = 'users'

    def __str__(self):
        return f'User(email={self.email})'
