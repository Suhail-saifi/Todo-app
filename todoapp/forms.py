from django import forms
from .models import *

class Todoform(forms.ModelForm):
    class Meta:
        model = Mytodo
        fields = ['task',]