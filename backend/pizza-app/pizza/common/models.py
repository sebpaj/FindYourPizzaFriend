from django.db import models

from users.models import User


class Pizza(models.Model):
    name = models.TextField(help_text="Custom pizza name", max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pizzas")


class Category(models.Model):
    name = models.TextField(help_text="Category of ingredient")


class Ingredient(models.Model):
    name = models.TextField(help_text="Ingredient of pizza", max_length=64)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name="ingredients"
    )
    pizza = models.ManyToManyField(Pizza, related_name="ingredients")
