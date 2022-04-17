from django.urls import path
from . import views

urlpatterns = [

    path('', views.PaperView.as_view(), name="paper"),
    path('feedback/<int:id>', views.FeedBackView.as_view(), name="feedback"),
    path('view-feedback/<int:id>', views.ViewFeedBack.as_view(), name="view_feedback"),

]