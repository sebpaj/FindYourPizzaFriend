import graphene

from .common.schema import CommonQuery


class Query(CommonQuery):
    pass


schema = graphene.Schema(query=Query)
