from django.urls import path

from . import views

urlpatterns = [
    # path('student/<my_id>/',views.dynamic, name = "detail"),
    path('<int:my_id>/',views.dynamic, name = "detail"),
    path('<int:my_id>/<int:my_subid>/',views.show_subdetails, name = "subdetail"),

]