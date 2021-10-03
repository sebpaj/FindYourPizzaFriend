import graphene


class UserWithSamePizzaType(graphene.ObjectType):
    id = graphene.String(required=True)
    pizza = graphene.String(required=True)