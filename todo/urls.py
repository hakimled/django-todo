from django.urls import path

from . import views

app_name = 'todo'

urlpatterns = [
    
    path('' , views.home , name='home'),
    path('task/<int:task_id>/done/', views.mark_done, name='mark_done'),
    path('task/<int:task_id>/delete/', views.delete_task, name='delete_task'),
    
]