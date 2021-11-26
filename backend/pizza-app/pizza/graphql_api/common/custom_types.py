import graphene

from graphql_api.users.types import UserType


class UserWithSamePizzaType(graphene.ObjectType):
    user = graphene.Field(UserType, required=True)
    pizza = graphene.String(required=True)
