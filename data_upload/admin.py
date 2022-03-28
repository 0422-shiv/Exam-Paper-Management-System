from django.contrib import admin
from .models import Semester, Course , ExamPaper 
# Register your models here.

admin.site.register(Semester)
admin.site.register(Course)
admin.site.register(ExamPaper)