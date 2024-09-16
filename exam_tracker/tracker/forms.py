from django import forms
from .models import Subject, ExamScore

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name']

from django import forms
from .models import Subject, ExamScore

class ExamScoreForm(forms.ModelForm):
    class Meta:
        model = ExamScore
        fields = ['subject', 'score', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})  # Use HTML5 date input
        }
