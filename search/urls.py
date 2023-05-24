from django.urls import path
from .views import search,home

urlpatterns = [
    path('', home, name='home'),
    path('search/', search, name='search'),
]
