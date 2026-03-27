from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('students/', views.student_list, name='student_list'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('subjects/', views.subject_list, name='subject_list'),
    path('holidays/', views.holiday_list, name='holiday_list'),
    path('exams/', views.exam_list, name='exam_list'),
]