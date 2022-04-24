from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from user.models import Role ,User
import random as r
from django.template.loader import get_template
import smtplib
import email.message
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from Exammanagment import settings
from django.urls import reverse_lazy
from django.contrib.auth.tokens import default_token_generator
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.utils.translation import gettext_lazy as _
from django.views.generic.edit import FormView
from .forms import PasswordResetForm
# Create your views here.


def authenticate(email=None, password=None, **kwargs):
    UserModel = User
    try:
        user = UserModel.objects.get(email=email,is_active=True)
    except UserModel.DoesNotExist:
        return None
    else:
        if user.check_password(password):
            return user
    return None

class LoginView(generic.TemplateView):
    template_name = "login.html"  

    def post(self, request,*args, **kwargs):
     
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f"Successfully logged in as {email}")  
            if request.user.is_authenticated:                       
                return HttpResponseRedirect(reverse('Dashboard:dashboard'))
        else:
            messages.error(request, "Invalid email or password.")
      
        return render(request, "login.html")    


class RegisterView(generic.TemplateView):
    template_name = "register.html"  
    def get(self, request):
        roles=Role.objects.all()
        return render(request,  "register.html",{'roles':roles})

    def post(self, request):
        name= request.POST.get('name')
        email= request.POST.get('email')
        role_id= request.POST.get('role')
        mobile_no= request.POST.get('mobile_number')
        password= request.POST.get('password')
        role=Role.objects.get(id=role_id)
        otp=""
        for i in range(4):
            otp+=str(r.randint(1,9))
        if User.objects.filter(mobile_no=mobile_no).exists():
            messages.error(request, 'Mobile Number Already taken')
            return HttpResponseRedirect(reverse('user:register'))
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email Already taken') 
            return HttpResponseRedirect(reverse('user:register'))
        user = User(fullname=name,email = email,role=role,mobile_no=mobile_no,is_terms_conditions=True)
        user.set_password(password)
        user.otp=otp
        user.save()
       
        data_content = {"otp": user.otp}

        email_content = 'email_template/email_to_new_user.html'

        email_template = get_template(email_content).render(data_content)
        reciver_email = email
       
        Subject = 'Account Verification'
        email_msg = EmailMessage(Subject, email_template, settings.EMAIL_HOST_USER, [reciver_email],
                                    reply_to=[settings.EMAIL_HOST_USER])
        email_msg.content_subtype = 'html'
        email_msg.send(fail_silently=False) 
        messages.success(request, "four digit code sent to your registered mail address")
        return render(request,  "verify.html",{"email":email})

class VerifyAccountView(generic.TemplateView):
    template_name = "verify.html" 
    
    def post(self,request) :
        code=request.POST.get("code")
        # email=request.POST.get("email")
        if User.objects.filter(otp=code).exists():
            User.objects.filter(otp=code).update(is_active=True)
            messages.info(request, 'Account Verified Successfully.')
            return HttpResponseRedirect(reverse('Dashboard:dashboard'))
        else:
            messages.error(request, 'Entered otp is wrong ,please enter again')
            return render(request, "verify.html")

@login_required
def LogoutPageView(request):
        logout(request)
        messages.info(request, "You have successfully logged out.")
        return HttpResponseRedirect(reverse('User:login'))


class PasswordContextMixin:
    extra_context = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': self.title,
            **(self.extra_context or {})
        })
        return context


class PasswordResetView(PasswordContextMixin, FormView):
    email_template_name = 'email_template/password_reset_email.html',
    extra_email_context = None
    form_class = PasswordResetForm
    from_email = settings.DEFAULT_FROM_EMAIL
    html_email_template_name = None
    subject_template_name = 'email_template/password_reset_subject.txt'
    success_url = reverse_lazy('password.reset.done')
    template_name ='password-reset/password_reset.html'
    title = _('Password reset')
    token_generator = default_token_generator

    @method_decorator(csrf_protect)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        
        opts = {
            'use_https': self.request.is_secure(),
            'token_generator': self.token_generator,
            'from_email': self.from_email,
            'email_template_name': self.email_template_name,
            'subject_template_name': self.subject_template_name,
            'request': self.request,
            'html_email_template_name': self.html_email_template_name,
            'extra_email_context': self.extra_email_context,
        }
        form.save(**opts)
        return super().form_valid(form)
    
