from graphene_federation import build_schema


from .common.schema import CommonQuery
from .users.schema import UsersQuery, UsersMutation


class Query(CommonQuery, UsersQuery):
    pass


class Mutation(UsersMutation):
    pass


schema = build_schema(query=Query, mutation=Mutation)
