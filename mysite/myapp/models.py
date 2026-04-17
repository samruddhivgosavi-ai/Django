from django.db import models

# Create your models here.
class Students(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    city=models.CharField(max_length=100,default="Pune")

class Employee(models.Model):
    emp_name=models.CharField(max_length=100)
    emp_email=models.CharField(max_length=100)
    emp_code=models.CharField(max_length=100)
    emp_phone=models.CharField(max_length=100)
    emp_designation=models.CharField(max_length=100)
    emp_salary=models.CharField(max_length=100)
    emp_address=models.CharField(max_length=100)
    emp_department=models.CharField(max_length=100,default="IT")

class document(models.Model):
    email=models.CharField(max_length=100)
    photo=models.FileField(upload_to='images')

class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    age = models.CharField(max_length=100)