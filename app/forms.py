from django import forms
from .models import jobappli,Profile

class jobappliform(forms.ModelForm):
    class Meta:
        model=jobappli
        fields=["comname","title","location","status","apldate","link","notes","deadline"]

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=["full_name","skills","bio"]