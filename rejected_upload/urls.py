from django.urls import path
from . import views

urlpatterns = [

    path('', views.RejectedUploadView.as_view(), name="RejectedUpload"),
    path('given-feedback/<int:id>', views.ViewGivenFeedBack.as_view(), name="given_feedback")

]