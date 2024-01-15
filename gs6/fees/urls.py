from django.urls import path
from . import views

urlpatterns = [
    path('feesdj/',views.fees_django),
    path('fesspython/',views.fees_python),
]