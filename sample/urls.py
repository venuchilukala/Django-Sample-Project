from django.urls import path
from .views import Home,result,course

urlpatterns =[
    path('',course),
    path('result',result)
]