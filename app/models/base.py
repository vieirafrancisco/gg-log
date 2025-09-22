"""Base model with UUID primary key."""
from tortoise.models import Model
from tortoise import fields


class BaseModel(Model):
    """
    Abstract base model with UUID primary key.
    """
    id = fields.UUIDField(primary_key=True)

    class Meta: # pylint: disable=missing-class-docstring
        abstract = True


class TimestampMixin:
    """
    Mixin to add created_at and updated_at timestamp fields.
    """
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
