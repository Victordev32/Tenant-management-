from django import forms
from .models import Tenant


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
      "first_name": forms.TextInput(attrs={"class":"outline-gray-400 bg-gray-200 p-2 focus:outline-gray-500 border-1 border-none block"}),
       "second_name": forms.TextInput(attrs={"class":"outline-gray-400 bg-gray-200 p-2 focus:outline-gray-500 border-1 border-none block"}),
       "email": forms.EmailInput(attrs={"class":"outline-gray-400 bg-gray-200 p-2 focus:outline-gray-500 border-1 border-none block"}),
       "phone_number": forms.TelInput(attrs={"class":"outline-gray-400 bg-gray-200 p-2 focus:outline-gray-500 border-1 border-none block","required":True})
       
    }
    