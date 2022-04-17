from django.db import models
from user.models import User
from data_upload.models import ExamPaper

# Create your models here.

class FeedBack(models.Model):
    feedback_by = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    exam_paper = models.ForeignKey(ExamPaper, on_delete=models.CASCADE,null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    return_feedback = models.BooleanField(default=True)
    status =models.BooleanField(default=False)
    is_updated =models.BooleanField(default=False)

    class Meta:
        verbose_name = 'FeedBack'
        verbose_name_plural = 'FeedBacks'

    def __str__(self) -> str:
        return self.exam_paper.subject