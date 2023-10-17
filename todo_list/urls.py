from django.urls import path, include
from . import views

urlpatterns = [
    # Add task Url
    path('add_task/', views.add_task, name='add_task'),
    # Mark as done Url
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
    # Mark as undone Url
    path('mark_as_undone/<int:pk>/', views.mark_as_undone, name='mark_as_undone'),
    # Edit task Url
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),

]