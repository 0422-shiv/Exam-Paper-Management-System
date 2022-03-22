from django.shortcuts import render
from django.views import generic

# Create your views here.


class SendNotificationView(generic.TemplateView):
    template_name = "send-notification.html"  