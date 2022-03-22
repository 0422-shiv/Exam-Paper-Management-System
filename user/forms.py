from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from user.models import RagisterUser



class UserForm(UserCreationForm):
                
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class RagisterForm(ModelForm):

    class Meta:
        model = RagisterUser
        fields = ['mobile_number', 'roll', 'address', 'term_condition']
                

