from django.contrib import admin
from .models import Semester, Course , ExamPaper ,Subjects
# Register your models here.

admin.site.register(Semester)
admin.site.register(Course)
admin.site.register(ExamPaper)
admin.site.register(Subjects)