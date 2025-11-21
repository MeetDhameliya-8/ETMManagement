from django.urls import path
from . import views

app_name = 'Screensite'

urlpatterns = [

    # Manager Dashboard
    path('manager/dashboard/', views.manager_dashboard, name='manager_dashboard'),
    path('manager/project/create/', views.create_project, name='create_project'),
    path('manager/project/<int:project_id>/assign/', views.assign_members, name='assign_members'),
    path('manager/project/<int:project_id>/', views.project_detail, name='project_detail'),

    path('manager/project/<int:project_id>/task/add/', views.add_task, name='add_task'),
    
]
