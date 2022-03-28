from django import forms
from .models import ExamPaper


class DataUploadForm(forms.ModelForm):
    class Meta:
        model = ExamPaper
        fields = ['semester', 'course', 'subject', 'subject_code', 'paper', 'status' ]