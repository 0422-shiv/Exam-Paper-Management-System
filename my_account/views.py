from django.shortcuts import render
from django.views import generic

# Create your views here.


class MyAccountView(generic.TemplateView):
    template_name = "my-account.html"  