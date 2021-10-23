import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoConnectionField

from .types import CategoryType, PizzaType


class CommonQuery(ObjectType):
    all_categories = DjangoConnectionField(CategoryType)
    
    pizza = relay.Node.Field(PizzaType)
    all_pizzas = DjangoConnectionField(PizzaType)

    

#TODO implrement resolver