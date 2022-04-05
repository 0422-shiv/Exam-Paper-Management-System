from django.http import JsonResponse
from django.shortcuts import render,get_object_or_404
from django.views import generic
from data_upload.models import Course, Semester,ExamPaper
from data_upload.forms import DataUploadForm
from django.contrib import messages
from django.http import  HttpResponseRedirect
from django.urls import reverse

# Create your views here.

class DataUploadView(generic.TemplateView):
    template_name = "data-upload.html" 

    def get(self, request):
        courses = Course.objects.all()
        semester = Semester.objects.all()
        return render(request,  "data-upload.html",{'courses':courses, 'semester':semester}) 

    def post(self,request):
        form = DataUploadForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()  
            messages.info(request, 'Your Data Successfully Upload.')
            return render(request, "data-upload.html")
        else:
            messages.info(request, 'Your Data has not Upload ! You fill the right Data')
            form = DataUploadForm()
        return render(request, "data-upload.html")  
    
class UpdateDataUploadView(generic.TemplateView):
    template_name = "edit-data-upload.html" 

    def get(self, request,id):
        instance=ExamPaper.objects.get(id=id)
        print(instance.subject)
        courses = Course.objects.all()
        semester = Semester.objects.all()
        return render(request,  "edit-data-upload.html",{'courses':courses, 'semester':semester,'instance':instance}) 

    def post(self, request, id, *args, **kwargs):
        data = get_object_or_404(ExamPaper, id=id)    
        form = DataUploadForm(request.POST, request.FILES or None, instance=data )
        if form.is_valid():
            form.save()
            messages.info(request, 'Your Data Successfully Updated.')        
            return HttpResponseRedirect(reverse('My-Upload:MyUploadView') ,{'form':form})  
        else:
            context = {"form": form , "data":data}
            messages.info(request, 'Your Data Not Updated')        
            return render(request, "edit-data-upload.html" , context)      
    
def DeleteDataView(request,id):
    print(id)
    ExamPaper.objects.filter(id=id).delete()
    return JsonResponse({'status':1})
    