from django.db import models


class Pizza(models.Model):
    name = models.TextField(help_text="Custom pizza name", max_length=64)


class Ingredient(models.Model):
    name = models.TextField(help_text="Ingredient of pizza", max_length=64)
    pizza = models.ManyToManyField(Pizza, related_name="pizzas")

