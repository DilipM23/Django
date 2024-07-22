from django.db import models

class course(models.Model): 
    course_code=models.CharField(max_length=40) 
    course_name=models.CharField(max_length=100) 
    course_credits=models.IntegerField() 
class student(models.Model): 
    student_usn=models.CharField(max_length=20) 
    student_name=models.CharField(max_length=100) 
    student_sem=models.IntegerField() 
    enrolment=models.ManyToManyField(course) 