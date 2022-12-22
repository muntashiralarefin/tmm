from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<str:district>/', views.home, name="home"),
    path('survey/', views.survey, name="survey"),
]
