from django import forms
from blog_app.models import *

class commentform(forms.ModelForm):
    comments = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'comment','placeholder':'Write Comment here..'}))
    class Meta:
        model = comment
        fields=['comments']
