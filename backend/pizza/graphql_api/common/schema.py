import graphene

class CommonQuery(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")

