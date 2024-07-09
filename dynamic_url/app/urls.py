from django.urls import path
from .views import home, profile

urlpatterns = [
	path('', home, name='home'),
	path('profile/<int:id>/', profile, {'status':200}, name='profile'),
]