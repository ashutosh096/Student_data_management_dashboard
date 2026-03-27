from django.contrib import admin
from .models import Student, Teacher, Department, Subject, Holiday, Exam

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Department)
admin.site.register(Subject)
admin.site.register(Holiday)
admin.site.register(Exam)