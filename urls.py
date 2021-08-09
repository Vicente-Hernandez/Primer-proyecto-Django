from django.urls import path     
from . import views


urlpatterns = [
    path('', views.root),
    path('mi_app/', views.index),
    path('mi_app/new/', views.new),
    path('mi_app/create/', views.create),
    path('mi_app/<int:number>/', views.show),
    path('mi_app/<int:number>/edit/', views.edit),
    path('mi_app/<int:number>/delete/', views.destroy),
    path('mi_app/json/', views.json),
    path('mi_app/imagen/', views.home),
    path('time_display/', views.time),
    path('user/<name>', views.user),
    path('random_word/', views.random_word),
    path('reset/', views.reset),
    path('login', views.login),
]
