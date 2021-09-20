from django.db import migrations


def forwards(apps, schema_editor):
    Ingredient = apps.get_model('common', 'Ingredient')
    Category = apps.get_model('common', 'Category')

    #TODO CONTINUE MIGRATION




def reverse(apps, schema_editor):
    Ingredient = apps.get_model('common', 'Ingredient')



class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_custom_categories'),
    ]

    operations = [
        migrations.RunPython(forwards, reverse),
    ]