from django.db import models
from .managers import CustomManager

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()

    # objects= models.Manager()
    # students =CustomManager()

class ProxyStudent(Student):
    students = CustomManager()
    class Meta:
        proxy = True
        ordering = ['name']
