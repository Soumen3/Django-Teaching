from django import forms
from .models import employee

class employeeForm(forms.ModelForm):
    addr = forms.CharField(widget=forms.Textarea(attrs={
        'class' : "form-control",
        'rows' : 3
    }))

    class Meta:
        model = employee
        fields = "__all__"
        labels= {
            'name': "Enter Name", 
            'email': "Enter Email",
        }

        help_texts = {
            'email': "Email must contain @ sign."
        }

        widgets = {
            'password':forms.PasswordInput(attrs={
                'class' : "form-control"
            }),
            'name': forms.TextInput(attrs={
                'class' : "form-control"
            })
        }
