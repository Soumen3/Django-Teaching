from django.shortcuts import render, redirect
from .forms import registrationForm, loginForm
from .models import employee
# Create your views here.
def user_login(request):
    context = {}
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = employee.objects.filter(username=username, password=password).first()

            if user :
                return redirect('home')

    form = loginForm()
    context['form'] = form
    return render(request, 'login.html', context)

def user_signup(request):
    context = {}
    if request.method == 'POST':
        form = registrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    form  = registrationForm()
    print(form)
    context['form'] = form
    return render(request, 'signup.html', context)

def home(request):
    return render(request, 'home.html')