from django.shortcuts import render, redirect
from django.contrib.auth.forms import  AuthenticationForm
from .forms import CustomeUserCreationForm
from django.contrib.auth import logout , authenticate, login
# Create your views here.

def home(request):
	return render(request, 'home.html')

def user_login(request):
	context = {
		'form': AuthenticationForm()
	}
	if request.method == "POST":
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			print(form.get_user())
			login(request, form.get_user())
			return redirect('home')
		else:
			return redirect('login')
	return render(request, 'login.html', context)

def register(request):
	context = {
		'form': CustomeUserCreationForm()
	}
	if request.method == "POST":
		form = CustomeUserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
		else:
			return redirect('register')
	return render(request, 'signup.html', context)

def logout_request(request):
	logout(request)
	return render(request, 'logoutView.html')