from django.urls import path
from . import views

app_name = "Screensite"

urlpatterns = [

    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('apply/', views.newjoinee_apply, name='apply'),
   
    path("mission/", views.mission, name="mission"),
    path('confirmation/', views.confirmation, name='confirmation'),
]

