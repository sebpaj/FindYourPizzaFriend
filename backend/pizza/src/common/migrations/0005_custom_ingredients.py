from django.db import migrations


def forwards(apps, schema_editor):
    Ingredient = apps.get_model('common', 'Ingredient')
    Category = apps.get_model('common', 'Category')

    cheeses_category = Category.objects.get(name="Cheeses")
    meat_category = Category.objects.get(name="Meat")
    sauce_category = Category.objects.get(name="Sauce")
    extras_category = Category.objects.get(name="Extras")
    vegetables_category = Category.objects.get(name="Vegetables")

    all_ingredients = []

    ingredients_mapping = {
        cheeses_category: [
            "Cheese", "Smoked ewe's milk cheese made in the Tatra Mountains", "Camembert", "Cheese XL", "Parmesan", "Feta"
            ],
        
        meat_category: [
            "Salami", "Ham", "Bacon", "Chicken", "Tuna", "Sausage", "Beaf"]
            ,
        sauce_category: [
            "Tomato", "Garlic", "BBQ", "Hot"
            ],
        extras_category: [
            "Fresh parsley", "Coriander", "Mayonnaise", "Arugula"
            ],
        vegetables_category: [
            "Mushrooms", "Onion", "Red Onion", "Corn", "Pickled cucumber", "Cucumber", "Pepper", "Broccoli", "Tomato", "Courgette"
            "Olives", "Spinach", "Pepperoni pepper", "Jalapeno pepper"
            ],
    }

    for category, ingredients in ingredients_mapping.items():
        for ingredient in ingredients:
            all_ingredients.append(Ingredient(name=ingredient, category=category))

    Ingredient.objects.bulk_create(all_ingredients)

def reverse(apps, schema_editor):
    Ingredient = apps.get_model('common', 'Ingredient')

    Ingredient.objects.all().delete()



class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_custom_categories'),
    ]

    operations = [
        migrations.RunPython(forwards, reverse),
    ]
