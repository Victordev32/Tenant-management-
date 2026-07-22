from django.urls import path
from . import views

urlpatterns=[
path("",views.apartments,name="apartments"),

path("add/",views.add_apartment,
     name="add_apartments"),
path("update/<int:apartment_id>",     views.update_apartment,name="update_apartment")
]