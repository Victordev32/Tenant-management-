from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from tenant_pages.models import Tenant
# Create your views here.
def dashboard(request):
    tenants=Tenant.objects.count()
    print(tenants)
    context={
      "tenants":tenants
    }
    return render(request,"super/dashboard.html",context)



