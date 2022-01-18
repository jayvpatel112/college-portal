from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# database----> excel workbook
# Models in Djago table -----> sheet

class paymentDetail(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=2000)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)
    fees = models.IntegerField(default=0)
    timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message from ' + self.name + ' - ' + self.email
