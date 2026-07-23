from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import Tenant
from .forms import TenantForm

# Create your views here.
def tenants(request):
    tenants=Tenant.objects.all()
    if request.method=="POST":
      tenant=Tenant.objects.get(id=request.POST["tenant_id"])
      if tenant:
        tenant.delete()
      
    return render(request,"tenants.html",{"tenants": tenants})

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
  return render(request,"add_tenant.html",{"form": form})

def update_tenant(request,tenant_id):
  tenant=get_object_or_404(Tenant,id=tenant_id)
  print(tenant)
  if request.method=="POST":
    form=TenantForm(request.POST,instance=tenant)
    if form.is_valid():
      form.save()
      messages.success(request,"<p class='bg-green-100 p-2>Tenant updated successfully</p>")
      return redirect("tenants")
    else:
      messages.error(request,"Fail to update tenant")
  else:
    form=TenantForm(instance=tenant)
  return render(request,"update_tenant.html",{"form": form})