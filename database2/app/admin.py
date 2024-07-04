from django.contrib import admin
from .models import Student, Teacher

# Register your models here.
# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
# 	list_display = ['id', 'name', 'age', 'grade']


# admin.site.register(Student)
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'age', 'grade']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'subject']