from django import forms
from .models import Find

class NewFind(forms.ModelForm):
    class Meta:
        model=Find
        fields=['title','body']