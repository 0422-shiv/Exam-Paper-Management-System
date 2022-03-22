from django.contrib import admin
from .models import RagisterUser
from django.contrib.admin.options import ModelAdmin


# Register your models here.


class RagisterAdmin(ModelAdmin):
    list_display = ["user", "mobile_number", "roll", "address", "term_condition"]

admin.site.register(RagisterUser,RagisterAdmin)