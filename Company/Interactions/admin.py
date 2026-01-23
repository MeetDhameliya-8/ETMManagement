
# Register your models here.
from django.contrib import admin
from .models import Communication


@admin.register(Communication)
class CommunicationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "update",
        "interaction_type",
        "created_by",
        "created_at",
    )

    list_filter = (
        "interaction_type",
        "created_at",
    )

    search_fields = (
        "message",
        "created_by__username",
        "update__Project",
    )

    readonly_fields = (
        "created_at",
    )

    ordering = ("-created_at",)
