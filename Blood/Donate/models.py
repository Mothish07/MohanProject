

from django.db import models

class Donor(models.Model):
    full_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=100) 
    blood_group = models.CharField(max_length=5)
    birth_date = models.DateField()
    gender = models.CharField(max_length=10)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    area = models.CharField(max_length=100)
    landmarks = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name
