from django.shortcuts import render
from django.views import generic

# Create your views here.


class ContactUsView(generic.TemplateView):
    template_name = "contact-us.html"  
