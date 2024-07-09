from django.shortcuts import render
from .form import regForm

# Create your views here.
def home(request):
	fm = regForm(auto_id="abcd", initial={'first_name': 'John', 'last_name': 'Doe', 'phone': 1234567890}, label_suffix="-")
	fm.order_fields(["first_name", "last_name", "phone", "email"])
	return render(request, 'home.html', {'form': fm})