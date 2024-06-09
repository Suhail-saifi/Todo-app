from django import forms
from .models import Mytodo

class Todoform(forms.ModelForm):
    class Meta:
        model = Mytodo
        fields = ['task']  # Exclude the user field
