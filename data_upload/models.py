from django.db import models
from user.models import User
# Create your models here.
class Semester(models.Model):
    semester_name = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Semester'
        verbose_name_plural = 'Semester'

    def __str__(self) -> str:
        return self.semester_name

class Course(models.Model):
    course_name = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Course'

    def __str__(self) -> str:
        return self.course_name
    
class Subjects(models.Model):
    subject_name = models.CharField(max_length=100, null=True, blank=True)
    subject_code = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'

    def __str__(self) -> str:
        return self.subject_name


class ExamPaper(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE,null=True, blank=True)
    course = models.ForeignKey(Course ,on_delete=models.CASCADE,null=True, blank=True)
    subject = models.CharField(max_length=50, null=True, blank=True)
    subject_code = models.CharField(max_length=20, null=True, blank=True)
    paper = models.FileField(upload_to='paper', null=True, blank=True)
    status = models.BooleanField(default=False)
    created_by =models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    paper_status= models.CharField(max_length=20,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return str(self.subject)