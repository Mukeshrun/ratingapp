from django.db import models
class Course(models.Model):
    course=models.CharField(max_length=50)
    def __str__(self):
        return f'{self.course}'
class Faculty(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    def __str__(self):
        return f'{self.name}'

class Student(models.Model):
    faculty=models.ForeignKey(Faculty,on_delete=models.CASCADE)
    course1=models.ForeignKey(Course,on_delete=models.CASCADE)
    student_name=models.CharField(max_length=50)
    rating=models.FloatField(default=0)
    def __str__(self):
        return f"Name {self.student_name} Rating {self.rating}"

class Teacher(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    def __str__(self):
        return f'Name{self.name} Email{self.email} Password {self.password}'
