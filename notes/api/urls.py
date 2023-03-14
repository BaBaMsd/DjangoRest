from django.urls import path
from . import views

urlpatterns = [
    path('', views.getNotes),
    path('notes/create', views.createNote),
    path('notes/update/<str:pk>/', views.updateNote),
    path('note/<str:pk>/', views.getNote),
    path('notes/delete/<str:pk>/', views.deletenote),
]