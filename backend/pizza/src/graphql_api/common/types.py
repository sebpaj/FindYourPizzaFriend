import graphene
from graphene import relay
from graphene_django.types import DjangoObjectType

from common.models import Category, Ingredient, Pizza

from .resolvers import resolve_users_with_same_pizza


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        interfaces = (relay.Node,)


class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        interfaces = (relay.Node,)


class PizzaType(DjangoObjectType):
    class Meta:
        model = Pizza
        interfaces = (relay.Node,)

    users_with_same_pizza = graphene.List(graphene.String, resolver=resolve_users_with_same_pizza)