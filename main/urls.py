from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('about/', views.about, name='about'),
    path('about2/', views.about2, name='about2'),
    path('employees/', views.employees, name='employees'),
    path('conferences/', views.conferences, name='conferences'),
    path('contacts/', views.contacts, name='contacts'),
]