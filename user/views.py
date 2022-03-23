from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from user.models import Role ,User
# Create your views here.


class LoginView(generic.TemplateView):
    template_name = "login.html"  

    # def post(self, request,*args, **kwargs):
    #     if request.method == "POST":
    #         form = User(request.POST)
    #         username = request.POST['username']
    #         password = request.POST['password']
    #         user = authenticate(username=username, password=password)
    #         print(user)
    #         if user is not None:
    #             login(request, user)
    #             messages.info(
    #                 request, f"You are now logged in as {username }.")  
    #             if request.user.is_authenticated:                       
    #                 return render(request, "dashboard.html")
    #         else:
    #             messages.error(request, "Invalid username or password.")
    #     else:
    #         messages.error(request, "Invalid username or password.")
    #     form = User()
    #     return render(request, "dashboard.html", {'form': form})    


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
        is_terms_conditions =request.POST.get('is_terms_conditions')
        role=Role.objects.get(id=role_id)
        user = User(fullname=name,email = email,role=role,mobile_no=mobile_no,is_terms_conditions=True)
        user.set_password(password)
        user.save()
        messages.success(request, "Account created successfully")
        return render(request,  "register.html")


@login_required
def LogoutPageView(request):
        logout(request)
        messages.info(request, "You have successfully logged out.")
        return render(request, "login.html" )