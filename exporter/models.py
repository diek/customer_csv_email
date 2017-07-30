from django.db import models


class Customers(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=20)
    company = models.CharField(max_length=80, default=None, blank=True, null=True)
    address = models.CharField(max_length=70)
    city = models.CharField(max_length=40)
    province = models.CharField(max_length=40, default=None, blank=True, null=True)
    country = models.CharField(max_length=40)
    postal_code = models.CharField(max_length=10, default=None, blank=True, null=True)
    phone = models.CharField(max_length=24, default=None, blank=True, null=True)
    fax = models.CharField(max_length=24, default=None, blank=True, null=True)
    email = models.CharField(max_length=60)

    def __str__(self):
        return '{}, {}'.format(self.last_name, self.first_name)
