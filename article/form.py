from .models import article
from django import forms
from django.forms import ModelForm

class addar(ModelForm):
    
    class Meta:
        model=article
        fields=[
        'title',
        'body',
        'pic',
        ]
