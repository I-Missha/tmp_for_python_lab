from django.urls import path
from . import views

urlpatterns = [
    path('', views.university_list, name='university_list'),
    path('create/', views.create_university, name='create_university'),
    path('delete/<int:univ_id>/', views.delete_university, name='delete_university'),
]