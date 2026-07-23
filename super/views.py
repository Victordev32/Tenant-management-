from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from tenant_pages.models import Tenant
from apartments.models import Apartment
# Create your views here.
@login_required
def dashboard(request):
    tenants=Tenant.objects.count()
    apartments=Apartment.objects.count()
    print(tenants)
    context={
      "tenants":tenants,
      "apartments": apartments
    }
    return render(request,"super/dashboard.html",context)



