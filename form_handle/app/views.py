from django.shortcuts import render

# Create your views here.

def home(request):
    if request.method == 'POST':
        data = request.POST
        print(data)
        print("name:", data['name'])
        print("Address:", data['address'])


    return render(request, 'home.html')
