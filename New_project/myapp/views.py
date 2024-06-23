from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    context ={
        "Name": "Sahil Kumar",
        "Age": 10,
        "Course":["Python", "Django", "JavaScript", "React"]
    }

    return render(request, "home.html", context)

def about(request):
    context={
        "Students":{
            "student1":{
                "Name": "Sahil Kumar",
                "Age": 10,
            },
            "student2":{
                "Name": "Amal Kumar",
                "Age": 20,
            },
            "student3":{
                "Name": "Aman Kumar",
                "Age": 30,
            },
        }
    }
    if request.method == "POST":
        # print(request.POST)
        name= request.POST.get("name")
        course= request.POST.get("course")
        print(name, course)
        context["name"]= name
        context["course"]= course

    # print(request.method)
    return render(request, "about.html", context)