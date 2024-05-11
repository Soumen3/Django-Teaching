from django.shortcuts import render

# Create your views here.
def home (request):
	# context is a dictionary which is used to send data to the template
	context={
		'name':'abcd',
		'age': 20,
		"job":'Programmer',
	}

	return render(request, 'home.html', context)

def about (request):
	return render(request, 'about.html')