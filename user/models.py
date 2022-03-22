from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# --------------------------------Ragister model----------------------------------
ROLL_CHOICES =(
    ("HOD", "HOD"),
    ("HOI", "HOI"),
    ("SETTER", "SETTER"),
)


class RagisterUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    mobile_number = models.IntegerField(null=True, blank=True)
    roll = models.CharField(max_length=25, null=True, blank=True, choices = ROLL_CHOICES , default='SETTER')
    address = models.TextField(null=True, blank=True)
    term_condition = models.BooleanField(null=True, blank=True)
    
    def __str__(self):
        return str(self.user)