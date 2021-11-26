# Generated by Django 3.2.7 on 2021-11-26 19:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0006_auto_20210928_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pizzas', to=settings.AUTH_USER_MODEL),
        ),
    ]