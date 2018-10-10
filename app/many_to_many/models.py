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

    # friend = models.ForeignKey(
    #     'self',
    #     blank=True,
    #     null=True,
    #     on_delete=models.SET_NULL,
    #     related_name='friend',
    #  )

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=80)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.CharField(max_length=80)
    invite_reason = models.CharField(max_length=80)
