from django.contrib import admin
from .models import University, Student

class UniversityAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_name', 'full_name', 'creation_date')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'birth_date', 'university', 'enrollment_year')

admin.site.register(University, UniversityAdmin)
admin.site.register(Student, StudentAdmin)
