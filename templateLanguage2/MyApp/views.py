from django.shortcuts import render

# Create your views here.
def home(request):
    cntxt={
        'students':{
            'student1':{
                "name":"Soumen",
                "age":22,
                "Courses": ["bca", 'mca', 'btech'],
            },
            'student2':{
                'name':"xyz",
                'age':20,
                "Courses":['bsc', 'msc', 'b.ed']
            }
        }
    }
    return render(request, 'home.html', context=cntxt)

def about(request):
    context={
        'name':'Soumen',
        'age':18,
        "Courses": ["bca"],
    }
    return render(request, 'about.html', context=context)


def contact(request):
    return render(request, 'contact.html')