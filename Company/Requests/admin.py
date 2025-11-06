
from django.contrib import admin
from .models import HRRequest

@admin.register(HRRequest)
class HRRequestAdmin(admin.ModelAdmin):
    list_display = ('applicant', 'hr_user', 'status', 'reviewed_at')
    list_filter = ('status',)
    search_fields = ('applicant__full_name', 'hr_user__email')

