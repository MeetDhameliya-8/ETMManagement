from django.urls import path
from .views import add_communication

app_name = "Interactions"

urlpatterns = [
    path(
        "employee-update/<int:update_id>/communicate/",
        add_communication,
        name="add_communication",
    ),
]
