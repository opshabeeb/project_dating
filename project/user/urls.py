from .views import *
from django.urls import path,include


urlpatterns = [
    path('',FirstView.as_view(),name='first'),
    path('signup',SignupView.as_view(),name='signup'),
    path('login',LoginView.as_view(),name='login'),
]