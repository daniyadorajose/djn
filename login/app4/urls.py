from django.urls import path
from app4 import views

urlpatterns = [
   path('',views.func,name="func"),
]