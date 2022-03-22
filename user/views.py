from django.shortcuts import render
from django.views import generic
from . forms import RagisterForm, UserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.contrib.auth.models import User

class LoginView(generic.TemplateView):
    template_name = "login.html"  

    def post(self, request,*args, **kwargs):
        if request.method == "POST":
            form = User(request.POST)
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                messages.info(
                    request, f"You are now logged in as {username }.")  
                if request.user.is_authenticated:                       
                    return render(request, "dashboard.html")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
        form = User()
        return render(request, "dashboard.html", {'form': form})    


class RegisterView(generic.TemplateView):
    template_name = "register.html"  
    form1 = UserForm()
    form2 = RagisterForm()

    def post(self, request,):
        if request.method == 'POST':
            form1 = UserForm(request.POST)
            form2 = RagisterForm(request.POST)
            print("********************************")
            if form1.is_valid():
                print(form1)
                if form2.is_valid():
                    print(form2)
                    saveform1 = form1.save()
                    saveform1.save()
                    saveform2 = form2.save(commit=False)
                    saveform2.user = saveform1
                    saveform2.save()
                    messages.success(request, f'Your account has been created ! You are now able to log in')                        
                return render(request, "dashboard.html" )
            else:
                form1 = UserForm()
                form2 = RagisterForm()
                messages.error(request, f'Your account has not created ! You fill the right information')                   
            return render(request,  "register.html" , {'form1': form1})


@login_required
def LogoutPageView(request):
        logout(request)
        messages.info(request, "You have successfully logged out.")
        return render(request, "login.html" )