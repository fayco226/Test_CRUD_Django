from django.urls import path
from . import views
urlpatterns = [
    path('', views.list_tasks, name="list_tasks"),
    path('add-task/', views.add_task, name="add-task"),
    path('update-task/<id>', views.update_task, name="update-task"),
    path('delete-task/<id>', views.delete_task, name="delete-task"),
]
