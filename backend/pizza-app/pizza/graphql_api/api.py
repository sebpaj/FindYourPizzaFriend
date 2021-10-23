from graphene_federation import build_schema


from .common.schema import CommonQuery


class Query(CommonQuery):
    pass


schema = build_schema(query=Query)
