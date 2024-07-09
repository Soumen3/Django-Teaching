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
	students = Student.objects.all()
	context = {'students': students}
	return render(request, 'home.html', context)

def profile(request, id, status):
	context ={}
	print("id ",id)
	print("status ",status)
	# students = Student.objects.all()
	students = Student.objects.filter(id=id)
	context['students'] = students
	return render(request, 'profile.html', context)