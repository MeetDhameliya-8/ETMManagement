from django import forms
from .models import Communication


class CommunicationForm(forms.ModelForm):
    class Meta:
        model = Communication
        fields = ["interaction_type", "message"]
        widgets = {
            "interaction_type": forms.Select(
                attrs={"class": "form-select"}
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Write your question / doubt / idea…"
                }
            ),
        }
