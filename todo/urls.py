from django.urls import path
from . import views

urlpatterns = [
    # Add new task
    path("addTask/", views.addTask, name='addTask'),

    # Mark task as done
    path("mark_as_done/<int:pk>/", views.mark_as_done, name='mark_as_done'),

    # Mark task as undone
    path("mark_as_undone/<int:pk>/", views.mark_as_undone, name='mark_as_undone'),

    # Edit selected task
    path("edit_task/<int:pk>/", views.edit_task, name='edit_task'),
]
