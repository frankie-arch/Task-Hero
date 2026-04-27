from django import forms
from .models import Task
from django.core.exceptions import ValidationError
from datetime import date

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'status', 'priority']
        widgets = {
            'due_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs.update({'class': 'form-control'})
        def clean_due_date(self):
            due_date = self.cleaned_data.get('due_date')
            if due_date and due_date < date.today():
                raise ValidationError("Due date cannot be in the past.")
            return due_date