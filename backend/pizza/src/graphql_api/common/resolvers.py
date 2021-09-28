from common.models import Pizza

def resolve_users_with_same_pizza(root, info):
    ingredients = root.ingredients.all().values_list("pk", flat=True)
    