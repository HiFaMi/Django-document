from django.db import models


class Topping(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=50)
    topping = models.ManyToManyField(
        Topping,
        related_name='pizzas',
    )

    def __str__(self):
        return self.name