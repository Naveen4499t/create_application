from django.db import models

# Create your models here.

class MYC(models.Model):
    mobile=models.IntegerField(unique=True)
    password=models.CharField(max_length=100,)
    confirmpassword=models.CharField(max_length=100)
    def __str__(self):
            return self.email


