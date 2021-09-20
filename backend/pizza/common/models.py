from django.db import models


class Pizza(models.Model):
    name = models.TextField(help_text="Custom pizza name", max_length=64)
    user = models.TextField(help_text="Author of pizza", max_length=64)


class Category(models.Model):
    name = models.TextField(help_text="Category of ingredient")


class Ingredient(models.Model):
    name = models.TextField(help_text="Ingredient of pizza", max_length=64)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    pizza = models.ManyToManyField(Pizza, related_name="pizzas")
    

