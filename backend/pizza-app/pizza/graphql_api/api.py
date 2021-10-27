from graphene_federation import build_schema


from .common.schema import CommonQuery
from .users.schema import UsersQuery


class Query(CommonQuery, UsersQuery):
    pass


schema = build_schema(query=Query)
