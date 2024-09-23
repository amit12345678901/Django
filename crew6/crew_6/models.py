from typing import Self
from django.db import models

# Create your models here.


class department(models.Model):
    name = models.CharField(max_length=100,null=False)
    location = models.CharField(max_length=100)
    
    def __str__(self):  
       return self.name  
    
     
class Role(models.Model):
    name = models.CharField(max_length=100, null=False)
     
    def __str__(self):
      return self.name 
    
    
class Employee(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100)
    dept = models.ForeignKey(department, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    hire_date = models.DateField()
    
    
      
    def __str__(self):
      return "%s %s %s" %(self.first_name, self.last_name, self.phone) 

class Carausel(models.Model):
    title = models.CharField(max_length=150)  
    description = models.TextField(max_length=100)  
    image = models.ImageField(upload_to='pics/%Y/%m/%d/')

    def __str__(self):  # This line should be indented consistently
        return self.title  # 4 spaces inside the method
