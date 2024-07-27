from django.shortcuts import render
from .forms import employeeForm
from .models import employee
# Create your views here.
def home(request):
    context = {}
    if request.method == 'POST':
        form = employeeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name'] 
            email = form.cleaned_data['email'] 
            
            employee.objects.create(name=name, email=email).save()
            

    form = employeeForm()
    context['form'] = form
    return render(request, 'home.html', context)