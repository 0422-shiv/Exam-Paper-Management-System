from django.shortcuts import render
from django.views import generic
from data_upload.models import ExamPaper
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import FeedBack 
from django.template.defaulttags import register
from send_notification.models import SendNotification
from user.models import User,Role
from django.db.models import Q
# Create your views here.

@method_decorator(login_required(login_url='/'), name="dispatch")
class PaperView(generic.TemplateView):
    template_name = "view-paper.html" 
    def get(self, request):
        dataupload=None
        if request.user.role.slug == 'hod' :
            dataupload = ExamPaper.objects.filter(
                course=request.user.assigned_course.first()).filter(Q(paper_status='Pending-HOD') | Q(paper_status='Approved') | Q(paper_status='Rejected-HOD')).order_by('-updated_at')
        elif request.user.role.slug == 'hoi' :
                dataupload = ExamPaper.objects.filter(
                course=request.user.assigned_course.first()).filter(Q(paper_status='Pending-HOI') | Q(paper_status='Approved') | Q(paper_status='Rejected-HOI')).order_by('-updated_at')
        return render(request,  "view-paper.html",{'dataupload':dataupload})  

@method_decorator(login_required(login_url='/'), name="dispatch")
class FeedBackView(generic.TemplateView):
    template_name = "feedback.html"  
    
    def post(self,request,id, *args, **kwargs): 
        comment = request.POST.get('comment')
        return_feedback = request.POST.get('return_feedback')
        status = request.POST.get('status')
     
        paper_data = ExamPaper.objects.get(id=id)
        form = FeedBack(comment = comment, return_feedback = return_feedback, feedback_by = request.user,
                        status=status, exam_paper=paper_data) 
        form.save()
        if status == 'True':
            if request.user.role.slug == 'hod' :
                paper_data.paper_status='Pending-HOI'
                notification=SendNotification.objects.create(send_notification_by=request.user,title=f'{paper_data.subject} paper is approved by HOD',
                            message=f'Your {paper_data.subject} paper is approved by HOD ,waiting for HOI approval')
                
           
            else:
                notification=SendNotification.objects.create(send_notification_by=request.user,title=f'{paper_data.subject} paper is approved by HOI',
                            message=f'Your {paper_data.subject} paper is successfully approved by HOI')
                paper_data.paper_status='Approved'
        else:
            if request.user.role.slug == 'hod' :
                    paper_data.paper_status='Rejected-HOD'
                    notification=SendNotification.objects.create(send_notification_by=request.user,title=f'{paper_data.subject} paper is rejected by HOD',
                            message=f'Your {paper_data.subject} paper is rejected by HOD ,Please check or upload again')
                
            else:
                paper_data.paper_status= 'Rejected-HOI'
                notification=SendNotification.objects.create(send_notification_by=request.user,title=f'{paper_data.subject} paper is rejected by HOI',
                            message=f'Your {paper_data.subject} paper is rejected by HOI ,Please check or upload again')
                
            
        notification.user.add(paper_data.created_by)
        paper_data.save()
        messages.info(request, 'Feedback sent successfully')
        return HttpResponseRedirect(reverse('View-Paper:paper'))
    

@register.filter(name='is_geedback_given')
def is_geedback_given(user,data):
    if FeedBack.objects.filter(feedback_by=user).filter(exam_paper=data).filter(is_updated=False).exists():
        return True
    return False

@method_decorator(login_required(login_url='/'), name="dispatch")
class ViewFeedBack(generic.TemplateView):
    template_name = "view-feedback.html" 
    def get(self, request,id):
        paper_data = ExamPaper.objects.get(id=id)
        feedback = FeedBack.objects.filter(feedback_by=request.user).filter(exam_paper=paper_data).last()
     
        return render(request,  self.template_name,{'feedback':feedback})  
