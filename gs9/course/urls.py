from django.urls import path
from . import views
urlpatterns = [
    path('leandj/',views.learn_django),
    path('learntimefilter/',views.learn_django_time),
    path('learnfloat/',views.lern_django_float),
    path('learntags/',views.learn_tags_python),
    path('learndotlookup/',views.learn_tags_dot_lookup),
    path('learnlooptag/',views.learn_loop_tags),
]