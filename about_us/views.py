from django.shortcuts import render
from django.views import generic

# Create your views here.


class AboutUsView(generic.TemplateView):
    template_name = "about.html"  
