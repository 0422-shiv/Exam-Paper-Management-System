from django.shortcuts import render
from django.views import generic
from data_upload.models import ExamPaper

# Create your views here.


class PaperView(generic.TemplateView):
    template_name = "view-paper.html" 
    def get(self, request):
        dataupload = ExamPaper.objects.all()
        return render(request,  "view-paper.html",{'dataupload':dataupload})  


class FeedBackView(generic.TemplateView):
    template_name = "feedback.html"  