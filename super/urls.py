from django.urls import path
from . import views

urlpatterns=[
  path("",views.dashboard,name="dashboard"),
  path("tenants/",views.tenants,name="tenants"),
  path("tenants/add",views.add_tenants,name="add_tenants"),
  path("tenants/update/<int:tenant_id>",views.update_tenant,name="update_tenant")
]