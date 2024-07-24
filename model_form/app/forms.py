from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        labels = {
            'name': 'Full Name',
            'age': 'Enter Age',
            'email': 'Enter Email',
            'dob': 'Date of Birth',
            'address': 'Addr'
        }
        help_texts={
            'age':"Age must be greater then 18"
        }

        widgets= {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
