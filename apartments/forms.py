from django import forms 
from .models import Apartment

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
