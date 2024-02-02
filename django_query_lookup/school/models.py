from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    roll = models.IntegerField()
    city = models.CharField(max_length=100)
    email = models.EmailField()
    marks = models.FloatField()
    passing_year = models.DateField()
    admissoon_date = models.DateTimeField()


    def __str__(self):
        return self.name
