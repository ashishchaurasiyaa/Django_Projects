from django.contrib import admin
from .models import ExamCenter, MyExamCenter
# Register your models here.

@admin.register(ExamCenter)
class ExamCenter(admin.ModelAdmin):
    list_display = ['id','cname', 'city']

@admin.register(MyExamCenter)
class MyExamCenter(admin.ModelAdmin):
    list_display = ['id','cname', 'city']
