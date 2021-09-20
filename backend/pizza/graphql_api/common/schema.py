import sys
print(sys.path)

import graphene

from common.models import Ingredient
from common.models import Category


class CommonQuery(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")
    ing = graphene.String()

    def resolve_ing(self, info):
        print(str(Ingredient.objects.all()))
        print(str(Category.objects.all()))


#TODO continue with graphne object
#TODO fix attempted relative improt beyond top level package