from django.urls import path
from . import views

urlpatterns = [
    path('', views.taskList, name='task-list'),
    path('create/', views.taskCreate, name='task-create'),
    path('edit/<str:pk>/', views.taskEdit, name='task-edit'), # Add this line
    path('update/<str:pk>/', views.taskUpdate, name='task-update'),
    path('delete/<str:pk>/', views.taskDelete, name='task-delete'),
]
