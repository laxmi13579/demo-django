from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.getPerson),
    path('add/',views.addPerson),
]