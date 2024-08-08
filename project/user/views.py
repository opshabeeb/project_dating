from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class FirstView(TemplateView):
    template_name = 'account/first.html'
    
class SignupView(TemplateView):
    template_name='account/signup.html'

class LoginView(TemplateView):
    template_name='account/login.html'
    
class ProfessionView(TemplateView):
    template_name='account/profession.html'
    
class Rel_GoalView(TemplateView):
    template_name='account/relationship_goal.html'
    
class InterestView(TemplateView):
    template_name='account/interested.html'
    
