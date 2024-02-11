from django import forms
from .models import *

class BlogpostForm(forms.ModelForm):
    class Meta():
        model=Blogpost
        fields=['title','content']

