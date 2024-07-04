from django.shortcuts import render , redirect
from .models import Student
# Create your views here.
def home(request):
	if request.method == 'POST':
		name = request.POST['name']
		age = request.POST['age']
		grade = request.POST['grade']

		Student(name=name, age=age, grade=grade).save()
		return redirect('profile')
	return render(request, 'home.html')

def profile(request):
	context ={}
	# students = Student.objects.all()
	students = Student.objects.filter(name="xyz")
	context['students'] = students
	return render(request, 'profile.html', context)