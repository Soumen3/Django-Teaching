from django.shortcuts import render

# Create your views here.
def home(request):
    cntxt={
        "name":"Soumen",
        "age":22,
        "Course": "MCA",
    }
    return render(request, 'home.html', context=cntxt)

def about(request):
    return render(request, 'about.html')