from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import SendNotification
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from user.models import User
from .forms import SendNotificationForm
# Create your views here.

@method_decorator(login_required(login_url='/'), name="dispatch")
class SendNotificationView(generic.TemplateView):
    template_name = "send-notification.html"  
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['user']=User.objects.filter(is_active=True)
        return context
    
    def post(self,request,*args, **kwargs):
        form = SendNotificationForm(request.POST)
       
        if form.is_valid():
            instance = form.save(commit=False)
            instance.send_notification_by = request.user
            instance.save()
            if 'user' in request.POST:
                for data in request.POST.getlist('user'):
                     instance.user.add(data)
            messages.info(request, 'Notification Sent Successful .')
            return HttpResponseRedirect(reverse('Send-Notification:sendnotification'))             
        else:
            messages.info(request, 'Your Notification has not Sent !fill the right information')
            print(form.errors)
            return HttpResponseRedirect(reverse('Send-Notification:sendnotification')) 
    

@method_decorator(login_required(login_url='/'), name="dispatch")
class AllNotificationView(generic.TemplateView):
    template_name = "notification.html"         

    def get(self, request):
        notification=SendNotification.objects.filter(user__in=[request.user]).order_by('-id')
        for data in notification:
            data.notification_status=True
            data.save()

        p = Paginator(notification, 8)  
        page_number = self.request.GET.get('page')
        try:
            page_obj = p.get_page(page_number) 
        except PageNotAnInteger:
            page_obj = p.page()
        except EmptyPage:
            page_obj = p.page(p.num_pages)

        return render(request, "notification.html",{'notification':notification, 'page_obj':page_obj})