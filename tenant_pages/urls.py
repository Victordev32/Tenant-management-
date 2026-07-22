from django.urls import path
from . import views

urlpatterns=[
  path("",views.tenants,name="tenants"),
  path("add",views.add_tenants,name="add_tenants"),
  path("update/<int:tenant_id>",views.update_tenant,name="update_tenant"),
  
]