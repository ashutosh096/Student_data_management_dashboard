from django.shortcuts import render
from .models import Student, Department, Teacher, Subject, Holiday, Exam

def dashboard(request):
    revenue = [100, 20, 30]  # example revenue data

    context = {
        'total_students': Student.objects.count(),
        'total_departments': Department.objects.count(),
        'total_teachers': Teacher.objects.count(),
        'total_subjects': Subject.objects.count(),
        'total_holidays': Holiday.objects.count(),
        'total_exams': Exam.objects.count(),
        'revenue': revenue,
    }
    return render(request, 'dashboard.html', context)


def student_list(request):
    query = request.GET.get('q', '')
    if query:
        students = Student.objects.filter(name__icontains=query)
    else:
        students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher_list.html', {'teachers': teachers})


def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'subjects.html', {'subjects': subjects})


def holiday_list(request):
    holidays = Holiday.objects.all()
    return render(request, 'holidays.html', {'holidays': holidays})


def exam_list(request):
    exams = Exam.objects.all()
    return render(request, 'exams.html', {'exams': exams})