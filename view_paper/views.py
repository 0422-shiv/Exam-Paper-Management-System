from django.shortcuts import render
from django.views import generic

# Create your views here.


class PaperView(generic.TemplateView):
    template_name = "view-paper.html"  


class FeedBackView(generic.TemplateView):
    template_name = "feedback.html"  