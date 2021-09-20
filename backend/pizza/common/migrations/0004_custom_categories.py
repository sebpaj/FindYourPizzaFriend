from django.db import migrations


def forwards(apps, schema_editor):
    Category = apps.get_model('common', 'Category')

    category_names = ["Cheeses", "Meat", "Sauce", "Spices", "Vegetables"]

    categories = [Category(name=name) for name in category_names]

    Category.objects.bulk_create(categories)
    

def reverse(apps, schema_editor):
    Category = apps.get_model('common', 'Category')

    Category.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_auto_20210920_2018'),
    ]

    operations = [
        migrations.RunPython(forwards, reverse),
    ]