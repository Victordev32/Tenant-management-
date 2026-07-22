from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import Apartment
from .forms import ApartmentForm
# Create your views here.
def apartments(request):
  apartments=Apartment.objects.all()
  return render(request,"apartments.html",{"apartments":apartments})
def add_apartment(request):
  if request.method=="POST":
    form=ApartmentForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request,"Apartment added successfully")
      redirect("apartments")
    else:
      messages.error(request," Fail to add apartment")
  else:
    form=ApartmentForm()
  return render(request,"add_apartment.html",{"form":form})
def update_apartment(request):
  return render(request,"update_apartment.html")
