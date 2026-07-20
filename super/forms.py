from django import forms
from .models import Tenant,Apartment


class TenantForm(forms.ModelForm):
  class Meta:
     model=Tenant
     fields=["first_name","second_name","email","phone_number"]
     labels={
       "first_name":"First name",
       "second_name":"Second name",
       "email":"Email address",
       "phone_number":"Phone number"
       
     }
     widgets={
      "first_name": forms.TextInput(attrs={"class":"outline-gray-400 bg-gray-200 p-2 focus:outline-gray-500 border-1 border-none block w-full"}),
       "second_name": forms.TextInput(attrs={"class":"outline-gray-400 bg-gray-200 p-2 focus:outline-gray-500 border-1 border-none block w-full"}),
       "email": forms.EmailInput(attrs={"class":"outline-gray-400 bg-gray-200 p-2 focus:outline-gray-500 border-1 border-none block w-full"}),
       "phone_number": forms.TelInput(attrs={"class":"outline-gray-400 bg-gray-200 p-2 focus:outline-gray-500 border-1 border-none block w-full","required":True})
       
    }

class ApartmentForm(forms.ModelForm):
  class Meta:
    model=Apartment
    fields=["name","location"]
    labels={
      "name":"Apartment name",
      "location":"Apartment location"
    }

    widgets={
      "name": forms.TextInput(attrs={"class":"outline-gray-400 bg-gray-200 p-2 focus:outline-gray-500 border-1 border-none block w-full"}),
       "location": forms.TextInput(attrs={"class":"outline-gray-400 bg-gray-200 p-2 focus:outline-gray-500 border-1 border-none block w-full"})
       
    }
