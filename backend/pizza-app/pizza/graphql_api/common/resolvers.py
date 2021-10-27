from typing import Dict
from collections import defaultdict

from common.models import Pizza

from .custom_types import UserWithSamePizzaType


def resolve_users_with_same_pizza(root, _):
    pizza_users: Dict[str, str] = defaultdict(str)

    for pizza in Pizza.objects.exclude(pk=root.id).iterator():
        root_ingredients = root.ingredients.all().values_list("name", flat=True)
        pizza_ingredients = pizza.ingredients.all().values_list("name", flat=True)
        if (
            root_ingredients.intersection(pizza_ingredients).count()
            == root_ingredients.count()
            == pizza_ingredients.count()
        ):
            pizza_users[pizza.user] = pizza.name

    result = [UserWithSamePizzaType(*args) for args in pizza_users.items()]

    return result
