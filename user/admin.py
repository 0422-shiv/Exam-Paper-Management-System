from django.contrib import admin
from .models import User,Role
from django.contrib.auth.models import Group

admin.site.register(User)
admin.site.register(Role)
admin.site.unregister(Group)