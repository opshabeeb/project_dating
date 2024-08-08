from .views import *
from django.urls import path,include


urlpatterns = [
    path('',FirstView.as_view(),name='first'),
    path('signup',SignupView.as_view(),name='signup'),
    path('login/',LoginView.as_view(),name='login'),
    path('profession',ProfessionView.as_view(),name='profession'),
    path('relationship_goal',Rel_GoalView.as_view(),name='relationship_goal'),
    path('interest',InterestView.as_view(),name='interest'),
  
]