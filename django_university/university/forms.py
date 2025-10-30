from django import forms
from .models import University, Student

class UniversityForm(forms.Form):
    full_name = forms.CharField(label="Полное название", max_length=200)
    short_name = forms.CharField(label="Сокращенное название", max_length=50)
    creation_date = forms.DateField(label="Дата создания", widget=forms.DateInput(attrs={'type': 'date'}))

class StudentForm(forms.Form):
    full_name = forms.CharField(label="ФИО", max_length=100)
    birth_date = forms.DateField(label="Дата рождения", widget=forms.DateInput(attrs={'type': 'date'}))
    university = forms.ModelChoiceField(label="Университет", queryset=University.objects.all())
    enrollment_year = forms.IntegerField(label="Год поступления")