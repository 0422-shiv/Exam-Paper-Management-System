from django.urls import path
from . import views

urlpatterns = [

    path('', views.RejectedUploadView.as_view(), name="RejectedUpload")

]