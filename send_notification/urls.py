from django.urls import path
from . import views

urlpatterns = [

    path('', views.SendNotificationView.as_view(), name="sendnotification"),
     path('all-notification', views.AllNotificationView.as_view(), name="allnotification"),

]