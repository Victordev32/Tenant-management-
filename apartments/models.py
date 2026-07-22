from django.db import models

# Create your models here.
class Apartment(models.Model):
  name=models.CharField(max_length=100)
  location=models.CharField(max_length=100)
  created_at=models.DateField(auto_now_add=True)
  updated_at=models.DateField(auto_now=True)

