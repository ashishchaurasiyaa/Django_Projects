from django.urls import path
from . import views

urlpatterns = [
    path('',views.base),
    path('home/',views.home),
    path('about/',views.about),
]