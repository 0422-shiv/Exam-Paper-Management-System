from django.shortcuts import render
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from data_upload.models import ExamPaper
from django.template.defaulttags import register
from send_notification.models import SendNotification
from django.template.loader import render_to_string
from django.db.models import Q
# Create your views here.

# class HomeView(generic.TemplateView):
#     template_name = "base_template.html"

@method_decorator(login_required(login_url='/'), name="dispatch")
class DashboardView(generic.TemplateView):
    template_name = "dashboard.html" 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dataupload'] = ExamPaper.objects.filter(created_by=self.request.user)[:5]
        context['status'] = ExamPaper.objects.filter(created_by=self.request.user).filter(Q(paper_status='Review-External-Examiner') | Q(paper_status='Review-Checker')).count()
        context['course'] = self.request.user.assigned_course.count()
        context['semester'] =self.request.user.assigned_semester.count()
        context['total_upload'] =ExamPaper.objects.filter(created_by=self.request.user).count()                 

        return context     
    

@register.filter(name='count_notification')
def count_notification(user):
    count = SendNotification.objects.filter(user__in =[user]).filter(notification_status=False).count()
    return count

@register.filter(name='get_new_notification')
def get_new_notification(user):
        get_data =SendNotification.objects.filter(user__in =[user]).filter(notification_status=False).order_by('-id')
        return render_to_string("new_notification.html", {"get_data": get_data})
              
  
