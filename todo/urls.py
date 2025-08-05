from django.urls import path

from . import views

app_name = 'todo'

urlpatterns = [
    
    path('' , views.home , name='task_list'),
    path('task/<int:task_id>/done/', views.mark_done, name='mark_done'),
    path('edit/<int:task_id>/', views.edit_task, name='update_task'),
    path('task/<int:task_id>/delete/', views.delete_task, name='delete_task'),
    path('add/', views.add_task, name='add_task'),
]