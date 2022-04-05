from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

urlpatterns = [

    path('', views.LoginView.as_view(), name="login"),
    path('register/', views.RegisterView.as_view(), name="register"),
    path('register', views.RegisterView.as_view(), name="register"),
    path('verify/', views.VerifyAccountView.as_view(), name="verify_account"),
    path('logout/', views.LogoutPageView, name="logout"),
     # Forget Password
    path('password-reset/',   views.PasswordResetView.as_view(success_url = reverse_lazy('User:password_reset_done')),name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='password-reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='password-reset/password_reset_confirm.html',
             success_url =  reverse_lazy('User:password_reset_complete')
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='password-reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),

]