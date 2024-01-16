from django.urls import path
from . import views

urlpatterns = [
    path('learnfee/',views.learn_fees),
]