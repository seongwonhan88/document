from django.db import models


# Create your models here.
class Topping(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=50)
    toppings = models.ManyToManyField(Topping)

    def __str__(self):
        return self.name


class FacebookUser(models.Model):
    name = models.CharField(max_length=50)
    friend = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='friend'
    )

    def __str__(self):
        return self.name
