from django.urls import path
from . import views


urlpatterns = [
	path('', views.home, name='home'),
	path('logout/', views.logout_request, name='logout'),
	path('login/', views.user_login, name='login'),
	path('register/', views.register, name='register'),
]