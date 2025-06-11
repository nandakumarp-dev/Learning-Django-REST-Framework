from django.urls import path 

from . import views

urlpatterns = [

    path('singers/',views.SingerListCreateView.as_view()),

    path('singers/<str:uuid>/',views.SingersRetrieveUpdateDestroyView.as_view()),

]
