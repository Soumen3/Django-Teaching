from django import forms
from .models import employee

class registrationForm(forms.ModelForm):
    class Meta:
        model = employee
        fields = "__all__"
        widgets = {
            'password': forms.PasswordInput(),
        }

class loginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)