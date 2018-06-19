from django.db import models

__all__ = (
    'Place',
    'Restaurant',
    'Supplier',
)


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return '[{}] place({})'.format(self.pk, self.name)


class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return '[{}] Restaurant'.format(self.pk)


class Supplier(Place):
    customers = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='supplier_by_customer',
        )
