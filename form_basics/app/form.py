from django import forms

class regForm(forms.Form):
	email = forms.EmailField()
	first_name = forms.CharField()
	last_name = forms.CharField()
	phone = forms.IntegerField()