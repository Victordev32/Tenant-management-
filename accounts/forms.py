from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
   email=forms.EmailField(label='Email address',widget=forms.EmailInput(attrs={"class":"outline-gray-400 bg-gray-200 p-2 focus:outline-gray-500 border-1 border-none block w-full"}))
   first_name=forms.CharField(label='First Name',widget=forms.TextInput(attrs={"class":"outline-gray-400 bg-gray-200 p-2 focus:outline-gray-500 border-1 border-none block w-full","required":True}))
   second_name=forms.CharField(label='Second name',widget=forms.TextInput(attrs={"class":"outline-gray-400 bg-gray-200 p-2 focus:outline-gray-500 border-1 border-none block w-full","required":True}))
   class meta:
    model=User
    fields=("username","email","first_name","second_name","password1","password2")
   def __init__(self,*args,**kwargs):
    super(SignUpForm,self).__init__(*args,
                                    **kwargs)
    self.fields["username"].widget.attrs["class"]="outline-gray-400 bg-gray-200 p-2 focus:outline-gray-500 border-1 border-none block w-full"
    self.fields["username"].widget.attrs["required"]=True
    self.fields["username"].label="Username"
    self.fields["password1"].widget.attrs["class"]="outline-gray-400 bg-gray-200 p-2 focus:outline-gray-500 border-1 border-none block w-full"
    self.fields["username"].help_text=""
    self.fields["password1"].widget.attrs["required"]=True
    self.fields["password1"].label="Password"
    self.fields["password1"].help_text="<li><small>Password should atleast 8 characters</small></li>"
    self.fields["password2"].widget.attrs["class"]="outline-gray-400 bg-gray-200 p-2 focus:outline-gray-500 border-1 border-none block w-full"
    self.fields["password2"].widget.attrs["required"]=True
    self.fields["password2"].label="Confirm Password"
    self.fields["password2"].help_text=""
 
   
