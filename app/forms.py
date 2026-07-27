from django import forms
from .models import jobappli,Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered!")
        return email
class jobappliform(forms.ModelForm):
    class Meta:
        model=jobappli
        fields=["comname","title","location","status","apldate","link","notes","examdate","ctc"]

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=["full_name","skills","bio"]