from graphene import ObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .types import UserType


class UsersQuery(ObjectType):
    users = DjangoFilterConnectionField(UserType)
