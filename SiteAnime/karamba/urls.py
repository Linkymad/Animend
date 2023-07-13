from django.urls import path
from .views import *
from . import views

urlpatterns = [
     path("", HomePage.as_view(), name='home_animend'),
     path('aniwill/', PageAniwill.as_view(), name='aniwill'),
     path('animend/', PageAnimend.as_view(), name='animend'),
     path('<slug:slug>/', views.AnimeDetailPage.as_view(), name='AnimeDetailPage'),

 ]
