from django.db import models

# Create your models here.
class course(models.Model):
    course_name=models.CharField(max_length=255)
    fee=models.IntegerField()
class student(models.Model):
    cours=models.ForeignKey(course,on_delete=models.CASCADE,null=True)
    student_name=models.CharField(max_length=255)
    student_address=models.CharField(max_length=255)
    student_age=models.IntegerField(null=True,blank=True,default=1)
    joining_date=models.DateField()