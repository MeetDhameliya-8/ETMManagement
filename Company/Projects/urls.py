from django.urls import path
from . import views

app_name = "Project"

urlpatterns = [
    path('dashboard/', views.manager_dashboard, name='manager_dashboard'),
    path('project/create/', views.create_project, name='create_project'),
    path('project/<int:project_id>/assign/', views.assign_members, name='assign_members'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('project/<int:project_id>/task/add/', views.add_task, name='add_task'),
]


