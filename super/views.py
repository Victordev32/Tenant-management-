from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import Tenant,Apartment
from .forms import TenantForm,ApartmentForm
# Create your views here.
def dashboard(request):
    tenants=Tenant.objects.count()
    print(tenants)
    context={
      "tenants":tenants
    }
    return render(request,"super/components/dashboard.html",context)

def tenants(request):
    tenants=Tenant.objects.all()
    if request.method=="POST":
      tenant=Tenant.objects.get(id=request.POST["tenant_id"])
      if tenant:
        tenant.delete()
      
    return render(request,"super/components/tenants.html",{"tenants": tenants})

def add_tenants(request):
  if request.method=="POST":
    form=TenantForm(request.POST)
    if form.is_valid():
      tenant=form.save()
      messages.success(request,"Tenant added successfully")
      return redirect("tenants")
    else:
      messages.error(request,"Fail to add tenant")
  else:
    form=TenantForm()
  return render(request,"super/components/add_tenant.html",{"form": form})

def update_tenant(request,tenant_id):
  tenant=get_object_or_404(Tenant,id=tenant_id)
  print(tenant)
  if request.method=="POST":
    form=TenantForm(request.POST,instance=tenant)
    if form.is_valid():
      form.save()
      messages.success(request,"Tenant updated successfully")
      return redirect("tenants")
    else:
      messages.error(request,"Fail to update tenant")
  else:
    form=TenantForm(instance=tenant)
  return render(request,"super/components/update_tenant.html",{"form": form})

def apartments(request):
  apartments=Apartment.objects.all()
  return render(request,"super/components/apartments.html",{"apartments":apartments})
def add_apartment(request):
  if request.method=="POST":
    form=ApartmentForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request,"Apartment added successfully")
      redirect("apartments")
    else:
      messages.error(request,"Fail to add apartment")
  else:
    form=ApartmentForm()
  return render(request,"super/components/add_apartment.html",{"form":form})
def update_apartment(request):
  return render(request,"super/components/update_apartment.html")
