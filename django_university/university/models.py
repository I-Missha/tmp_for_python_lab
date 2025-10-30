from django.db import models

class University(models.Model):
    full_name = models.CharField(verbose_name="Полное название", max_length=200)
    short_name = models.CharField(verbose_name="Сокращенное название", max_length=50)
    creation_date = models.DateField(verbose_name="Дата создания")

    def __str__(self):
        return self.short_name

class Student(models.Model):
    full_name = models.CharField(verbose_name="ФИО", max_length=100)
    birth_date = models.DateField(verbose_name="Дата рождения")
    university = models.ForeignKey(University, on_delete=models.CASCADE, verbose_name="Университет")
    enrollment_year = models.IntegerField(verbose_name="Год поступления")

    def __str__(self):
        return self.full_name
