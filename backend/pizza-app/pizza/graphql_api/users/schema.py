from graphene import ObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .mutations.log_in_mutation import LoginMutation
from .types import UserType


class UsersQuery(ObjectType):
    users = DjangoFilterConnectionField(UserType)


class UsersMutation(ObjectType):
    login = LoginMutation.Field()
