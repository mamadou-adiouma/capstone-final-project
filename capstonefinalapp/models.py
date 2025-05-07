from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
# class User(models.Model):
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=50)


class MenuItem(models.Model):
    image = models.CharField(max_length=150)
    name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return f'{self.name, self.price}'


class Booking(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=50)
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(default=10)

    # https://django-phonenumber-field.readthedocs.io/en/latest/reference.html
    phone_number = PhoneNumberField(blank=True, null=True)
    email = models.EmailField(max_length=150, unique=True)

    def __str__(self):
        return f'{self.first_name, self.reservation_date}'