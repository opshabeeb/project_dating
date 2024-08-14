from .views import *
from django.urls import path,include


urlpatterns = [
    path('',FirstView.as_view(),name='first'),
    path('signup',SignupView.as_view(),name='signup'),
    path('login/',LoginView.as_view(),name='login'),
    path('profession',ProfessionView.as_view(),name='profession'),
    path('relationship_goal',Rel_GoalView.as_view(),name='relationship_goal'),
    path('interest',InterestView.as_view(),name='interest'),
    
    path('create_group',CreateGroupView.as_view(),name='create_group'),
    path('groupslist',GroupListView.as_view(),name='group_list'),
    
    path('subscriptionplan/', SubscriptionPlanView.as_view(), name='subscription_plan'),
    path('paymentmethods/', PaymentMethodsView.as_view(), name='payment_methods'),
    path('addpaymentmethods/', AddPaymentMethodsView.as_view(), name='add_payment_methods'),
  
]