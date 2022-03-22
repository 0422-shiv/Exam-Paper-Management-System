from django.urls import path
from . import views

urlpatterns = [

    path('', views.MyAccountView.as_view(), name="myaccount")

]