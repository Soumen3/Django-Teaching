from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .froms import userSingupForm
# Create your views here.

def home(request):
	return render(request, 'home.html')

def user_login(request):
	context={}
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				context['form'] = form
				return render(request, 'login.html', context)
	context['form'] = AuthenticationForm()
	return render(request, 'login.html', context)

def user_signup(request):
	context = {}
	if request.method == 'POST':
		form = userSingupForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	form = userSingupForm()
	context['form'] = form
	return render(request, 'signup.html', context)

def user_logout(request):
	logout(request)
	return redirect('home')