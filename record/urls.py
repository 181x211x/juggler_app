

# coding: utf-8
from rest_framework import routers
from .views import RecordViewSet
from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from .views import SignUp




urlpatterns = [
    path('templates/', views.top,name='top'),
    path('login/', auth_views.LoginView.as_view(template_name='record/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('create/', views.record_forms,name='record_forms'),
    path('signup/', SignUp.as_view(template_name='record/signup.html'), name='signup'),
    path('all_record/', views.all_record,name='all_record'),
    path('result/', views.result,name='result'),
    path('rank/', views.rank,name='rank'),

]

router = routers.DefaultRouter()
router.register(r'records', RecordViewSet)
