from django.urls import path
from . import views

urlpatterns = [

    path('', views.ContactUsView.as_view(), name="contactus")

]