from django.db import models

# Create your models here.
class Tenant(models.Model):
  first_name=models.CharField(max_length=100)
  second_name=models.CharField(max_length=100)
  email=models.EmailField()
  phone_number=models.IntegerField()
  created_at=models.DateField(auto_now_add=True)
  updated_at=models.DateField(auto_now=True)


  def __str__(self):
     return f'{{self.first_name}} {{self.second_name}}'

class Apartment(models.Model):
  name=models.CharField(max_length=100)
  location=models.CharField(max_length=100)
  created_at=models.DateField(auto_now_add=True)
  updated_at=models.DateField(auto_now=True)



