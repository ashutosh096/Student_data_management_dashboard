from django.db import models

# Departments
class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Students
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    roll_number = models.IntegerField(default=1)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    fees_submitted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.roll_number})"

# Teachers
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    salary = models.FloatField(default=0)

    def __str__(self):
        return f"{self.name} ({self.salary})"

# Subjects
class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Holidays
class Holiday(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.date})"

# Exams
class Exam(models.Model):
    name = models.CharField(max_length=50)  # Mid1, Mid2
    date = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.date})"