from django.forms import ModelForm
from django import forms
from .models import Player

class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = '__all__'
        
