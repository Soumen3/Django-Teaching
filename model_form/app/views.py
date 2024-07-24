from django.shortcuts import render
from .forms import StudentForm

# Create your views here.
def home(request):
    context={}
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        
    form = StudentForm()
    context ['form'] = form
    return render(request, 'home.html', context)