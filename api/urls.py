"""notesapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_routes, name = 'routes'),
    path('notes/', views.get_notes, name = 'notes'),
    path('notes/create/', views.create_note, name = 'create-note'),
    path('notes/<str:pk>/update/', views.update_note, name = 'update-note'),
    path('notes/<str:pk>/delete/', views.delete_note, name = 'delete-note'),
    path('notes/<str:pk>/', views.get_note, name = 'note'),
    
    
]
