from django.shortcuts import render
from django.views import generic

# Create your views here.

class RejectedUploadView(generic.TemplateView):
    template_name = "rejected-upload.html"