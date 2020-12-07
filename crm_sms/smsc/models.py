from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    register_id = models.DateTimeField()
    first_name = models.TextField(max_length=255)
    last_name = models.TextField(max_length=255)
    age = models.IntegerField()
    email = models.TextField(max_length=50, null=True)
    mobile = models.TextField(max_length=255)
    phone = models.TextField(max_length=255)
    address = models.TextField(max_length=255)

    def __str__(self):
        return(f"{self.customer_id}-{self.first_name} {self.last_name}")