from django.urls import path
from . import views

urlpatterns = [

    path('', views.AboutUsView.as_view(), name="aboutus")

]