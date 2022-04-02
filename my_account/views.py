from django.shortcuts import render
from django.views import generic
from user.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
import os
from .forms import MyPasswordChangeForm
from django.contrib.auth import update_session_auth_hash
# Create your views here.


class MyAccountView(generic.TemplateView):
    template_name = "my-account.html"  
 
    def get(self,request) :
        user=User.objects.get(id=self.request.user.id)
        return render(request,self.template_name,{"user":user})
    
    def post(self,request):
        if request.POST.get("form_type") == "profile":
            fullname= request.POST.get("fullname")
           
            email= request.POST.get("email")
            address= request.POST.get("address")
            phone= request.POST.get("phone")
            if User.objects.filter(mobile_no=phone).filter(~Q(mobile_no=request.user.mobile_no)).exists():
                messages.error(request, 'Mobile Number Already taken')
                return HttpResponseRedirect(reverse('My-Account:myaccount'))
            if User.objects.filter(email=email).filter(~Q(email=request.user.email)).exists():
                messages.error(request, 'Email Already taken') 
                return HttpResponseRedirect(reverse('My-Account:myaccount'))
            User.objects.filter(id=request.user.id).update(
                                            fullname=fullname,
                                                    email=email,
                                                    address=address,
                                                    mobile_no=phone)
            if "img" in request.FILES:
                user=request.user
                if user.img:
                    image_path=user.img.path
                
                    if os.path.exists(user.img.path):
                        os.remove(image_path)
                        user.img=request.FILES["img"]
                        user.save()
                else:
                    user.img=request.FILES["img"]
                    user.save()
             
            messages.success(request,"successfully updated ")
        elif 'change_password' in request.POST:
            form = MyPasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(request, "Your password was successfully updated")
            else:
                messages.error(request, form.errors)
		   
        return HttpResponseRedirect(reverse('My-Account:myaccount'))
    
    