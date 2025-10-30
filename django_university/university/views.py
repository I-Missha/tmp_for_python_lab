from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect, HttpResponseNotFound
from . import forms
from . import models

def university_list(request):
    all_universities = models.University.objects.all()
    data = {"universities": all_universities}
    return TemplateResponse(request, "university_list.html", data)

def create_university(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        short_name = request.POST.get("short_name")
        creation_date = request.POST.get("creation_date")
        university = models.University.objects.create(
            full_name=full_name,
            short_name=short_name,
            creation_date=creation_date
        )
        return HttpResponseRedirect("/university/")
    else:
        data = {"form": forms.UniversityForm()}
        return TemplateResponse(request, "create_university.html", data)

def delete_university(request, univ_id):
    try:
        university = models.University.objects.get(id=univ_id)
        university.delete()
        return HttpResponseRedirect("/university/")
    except models.University.DoesNotExist:
        return HttpResponseNotFound("Университета с таким id не существует")

def student_list(request):
    all_students = models.Student.objects.all()
    data = {"students": all_students}
    return TemplateResponse(request, "student_list.html", data)

def create_student(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        birth_date = request.POST.get("birth_date")
        university_id = request.POST.get("university")
        enrollment_year = request.POST.get("enrollment_year")
        
        university = models.University.objects.get(id=university_id)
        student = models.Student.objects.create(
            full_name=full_name,
            birth_date=birth_date,
            university=university,
            enrollment_year=enrollment_year
        )
        return HttpResponseRedirect("/student/")
    else:
        data = {"form": forms.StudentForm()}
        return TemplateResponse(request, "create_student.html", data)

def delete_student(request, student_id):
    try:
        student = models.Student.objects.get(id=student_id)
        student.delete()
        return HttpResponseRedirect("/student/")
    except models.Student.DoesNotExist:
        return HttpResponseNotFound("Студента с таким id не существует")
