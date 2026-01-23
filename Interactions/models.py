
# Create your models here.
from django.db import models
from django.conf import settings
from Projects.models import EmployeeUpdate


class Communication(models.Model):
    QUESTION = "question"
    DOUBT = "doubt"
    PROBLEM = "problem"
    REASON = "reason"
    IDEA = "idea"

    INTERACTION_TYPES = [
        (QUESTION, "Question"),
        (DOUBT, "Doubt"),
        (PROBLEM, "Problem"),
        (REASON, "Reason"),
        (IDEA, "Idea"),
    ]

    update = models.ForeignKey(
        EmployeeUpdate,
        on_delete=models.CASCADE,
        related_name="interactions"
    )

    interaction_type = models.CharField(
        max_length=20,
        choices=INTERACTION_TYPES
    )

    message = models.TextField()

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_interaction_type_display()} by {self.created_by}"
