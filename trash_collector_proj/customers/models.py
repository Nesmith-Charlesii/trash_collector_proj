from django.db import models


# Create your models here.

# TODO: Finish customer model by adding necessary properties to fulfill user stories


class Customer(models.Model):
    name = models.CharField(max_length=50)
    weekly_pickup = models.CharField(max_length=50, null=True)
    one_time_pickup = models.DateField(null=True, blank=True)
    balance = models.IntegerField()
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    address = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name