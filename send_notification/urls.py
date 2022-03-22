from django.urls import path
from . import views

urlpatterns = [

    path('', views.SendNotificationView.as_view(), name="sendnotification")

]