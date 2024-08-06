from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class FirstView(TemplateView):
    template_name = 'account/first.html'
    
class SignupView(TemplateView):
    template_name='account/signup.html'

class LoginView(TemplateView):
    template_name='account/login.html'