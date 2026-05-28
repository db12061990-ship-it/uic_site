from django.urls import path
from .views import research_list

urlpatterns = [
    path('', research_list, name='research'),
]