from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Tenant
from .forms import TenantForm
# Create your views here.
def dashboard(request):
    return render(request,"super/components/dashboard.html")

def tenants(request):
    tenants=Tenant.objects.all()
    if request.method=="POST":
      print(request.POST.tenant_id)
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

