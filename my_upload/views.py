from django.shortcuts import render
from django.views import generic
from data_upload.models import ExamPaper
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.

@method_decorator(login_required(login_url='/'), name="dispatch")
class MyUploadView(generic.TemplateView):
    template_name = "my-upload.html" 

    def get(self, request):
        uploaded_papers = ExamPaper.objects.filter(created_by=request.user).order_by('-id')
        return render(request,  "my-upload.html",{'uploaded_papers':uploaded_papers})  

   