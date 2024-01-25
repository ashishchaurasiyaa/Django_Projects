from django.urls import path,register_converter

from . import views,converters
register_converter(converters.FourDigitConverter,'yyyy')

urlpatterns = [
    path('session/<yyyy:year>/',views.dynamic, name="subdetail"),

]