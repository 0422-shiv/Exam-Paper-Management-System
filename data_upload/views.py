from django.http import JsonResponse
from django.shortcuts import render,get_object_or_404
from django.views import generic
from data_upload.models import Course, Semester,ExamPaper,Subjects
from data_upload.forms import DataUploadForm
from django.contrib import messages
from django.http import  HttpResponseRedirect
from django.urls import reverse
from user.models import User,Role
from send_notification.models import SendNotification
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from view_paper.models import FeedBack

# Create your views here.
@method_decorator(login_required(login_url='/'), name="dispatch")
class DataUploadView(generic.TemplateView):
    template_name = "data-upload.html" 

    def get(self, request):
        courses = request.user.assigned_course.all()
        semester = request.user.assigned_semester.all()
        subjects=Subjects.objects.all()
       
        return render(request,  "data-upload.html",{'courses':courses, 'semester':semester,'subjects':subjects}) 

    def post(self,request):
        form = DataUploadForm(request.POST, request.FILES)
        
        if form.is_valid():
            instance = form.save(commit=False)
            
            if not form.cleaned_data['course'] or not form.cleaned_data['semester']:
                messages.error(request, 'Your Data has not Upload ! You fill the right Data')
                return render(request, "data-upload.html")
            instance.created_by = request.user
            instance.paper_status = 'Pending-Checker'
            instance.save() 
            role= Role.objects.get(slug='hod')
           
            notification=SendNotification.objects.create(send_notification_by=request.user,title='New Paper to view',message=f'{request.user} uploaded new paper of {instance.course} of {instance.semester}')
            [notification.user.add(data) for data in User.objects.filter(assigned_course__in=[instance.course]).filter(assigned_semester__in=[instance.semester]).filter(role=role)]
           
            messages.info(request, 'Your Data Successfully Upload.')
            return render(request, "data-upload.html")
        else:
            messages.info(request, 'Your Data has not Upload ! You fill the right Data')
            form = DataUploadForm()
        return render(request, "data-upload.html")  

@method_decorator(login_required(login_url='/'), name="dispatch")   
class UpdateDataUploadView(generic.TemplateView):
    template_name = "edit-data-upload.html" 

    def get(self, request,id):
        instance=ExamPaper.objects.get(id=id)
        
        courses = request.user.assigned_course.all()
        semester = request.user.assigned_semester.all()
        subjects=Subjects.objects.all()
        return render(request,  "edit-data-upload.html",{'subjects':subjects,'courses':courses, 'semester':semester,'instance':instance}) 

    def post(self, request, id, *args, **kwargs):
        data = get_object_or_404(ExamPaper, id=id)    
        form = DataUploadForm(request.POST, request.FILES or None, instance=data )
        if form.is_valid():
            form.save()
            paper_data = ExamPaper.objects.get(id=id)
            role =Role.objects.get(slug='hoi')
            if FeedBack.objects.filter(exam_paper=paper_data).exists():
                feedback = FeedBack.objects.filter(exam_paper=paper_data).last()
                if feedback.return_feedback and feedback.feedback_by.role.slug == 'hod':
                    feedback.is_updated = True
                    notification=SendNotification.objects.create(send_notification_by=request.user,
                                    title = f'{paper_data.subject} paper is updated to review',
                                    message=f'{request.user} is updated {paper_data.subject} , Give feedback')
                    notification.user.add(feedback.feedback_by)
                    paper_data.paper_status = 'Pending-Checker'
                    
                elif feedback.return_feedback  == False and feedback.feedback_by.role.slug == 'hod':
                    notification=SendNotification.objects.create(send_notification_by=request.user,
                                    title = f'{paper_data.subject} paper is updated to review',
                                    message=f'{request.user} is updated {paper_data.subject} , Give feedback')
                    [notification.user.add(data) for data in User.objects.filter(role=role)]
                    paper_data.paper_status = 'Pending-External-Examiner'
                elif feedback.return_feedback and feedback.feedback_by.role.slug == 'hoi':
                    feedback.is_updated = True
                    notification=SendNotification.objects.create(send_notification_by=request.user,
                                    title = f'{paper_data.subject} paper is updated to review',
                                    message=f'{request.user} is updated {paper_data.subject} , Give feedback')
                    notification.user.add(feedback.feedback_by)
                    paper_data.paper_status = 'Pending-External-Examiner'
                else:
                    paper_data.paper_status = 'Excellent'
                feedback.save()    
                    
            paper_data.save()
            messages.info(request, 'Your Data Successfully Updated.')        
            return HttpResponseRedirect(reverse('My-Upload:MyUploadView') ,{'form':form})  
        else:
            context = {"form": form , "data":data}
            messages.info(request, 'Your Data Not Updated')        
            return render(request, "edit-data-upload.html" , context)      
  
def DeleteDataView(request,id):
  
    ExamPaper.objects.filter(id=id).delete()
    return JsonResponse({'status':1})
    