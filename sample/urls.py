from django.urls import path
from .views import Home,result,course,validate,signup,login

urlpatterns =[
    path('',validate),
    path('result',result),
    path('signup',signup),
    path('login',login),
    
]