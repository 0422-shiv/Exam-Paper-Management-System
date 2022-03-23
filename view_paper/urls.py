from django.urls import path
from . import views

urlpatterns = [

    path('', views.PaperView.as_view(), name="paper"),
    path('feedback', views.FeedBackView.as_view(), name="feedback")

]