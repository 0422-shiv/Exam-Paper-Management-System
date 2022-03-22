from django.shortcuts import render
from django.views import generic
# Create your views here.


class MyUploadView(generic.TemplateView):
    template_name = "my-upload.html"  

   