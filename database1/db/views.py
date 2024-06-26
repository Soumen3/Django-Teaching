from django.shortcuts import render
from .models import Student
from django.contrib.auth.models import User

# Create your views here.
def home(request):

	context = {}

	if request.method=="POST":
		# print(request.POST)
		name=request.POST['name']
		age=request.POST['age']
		grade=request.POST['grade']
		print(name,age,grade)
		Student(name=name,age=age,grade=grade).save()
		

	students = Student.objects.filter(grade='a')
	print(students)
	context = {'students':students}
	return render(request, 'home.html', context)