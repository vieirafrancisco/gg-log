from tortoise.models import Model
from tortoise import fields


class User(Model):
    id = fields.UUIDField(pk=True)
    email = fields.CharField(max_length=100, unique=True)
    password_hash = fields.CharField(max_length=128)
    is_active = fields.BooleanField(default=True)

    class Meta:
        table = 'users'

    def __str__(self):
        return 'User(email={})'.format(self.email)
