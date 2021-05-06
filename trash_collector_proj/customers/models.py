from django.db import models


# Create your models here.

# TODO: Finish customer model by adding necessary properties to fulfill user stories


class Customer(models.Model):
    name = models.CharField(max_length=50)
    weekly_pickup = models.CharField(max_length=50)
    one_time_pickup = models.DateField()
    balance = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    address = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    #  password = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
