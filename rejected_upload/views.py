from django.shortcuts import render
from django.views import generic
from data_upload.models import ExamPaper
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from view_paper.models import FeedBack
# Create your views here.

@method_decorator(login_required(login_url='/'), name="dispatch")   
class RejectedUploadView(generic.TemplateView):
    template_name = "rejected-upload.html"
    
    def get(self, request,*args, **kwargs):
        rejected = ExamPaper.objects.filter(created_by=request.user).filter(Q(paper_status='Review-External-Examiner') | Q(paper_status='Review-Checker')).order_by('-id')

        return render(request,  "rejected-upload.html",{'rejected':rejected}) 
    
@method_decorator(login_required(login_url='/'), name="dispatch")
class ViewGivenFeedBack(generic.TemplateView):
    template_name = "view-feedback.html" 
    def get(self, request,id):
        paper_data = ExamPaper.objects.get(id=id)
        feedback = FeedBack.objects.filter(exam_paper=paper_data).last()
     
        return render(request,  self.template_name,{'feedback':feedback})  