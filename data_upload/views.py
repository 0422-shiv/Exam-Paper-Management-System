from django.shortcuts import render
from django.views import generic

# Create your views here.


class DataUploadView(generic.TemplateView):
    template_name = "data-upload.html"  
