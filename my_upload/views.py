from django.shortcuts import render
from django.views import generic
from data_upload.models import ExamPaper
# Create your views here.


class MyUploadView(generic.TemplateView):
    template_name = "my-upload.html" 

    def get(self, request):
        uploaded_papers = ExamPaper.objects.all()
        return render(request,  "my-upload.html",{'uploaded_papers':uploaded_papers})  

   