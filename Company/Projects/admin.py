# Register your models here.
from django.contrib import admin
from .models import Project, Task

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'manager', 'deadline', 'status', 'created_at')
    list_filter = ('status', 'deadline', 'manager')
    search_fields = ('title', 'manager__email')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'status')
    list_filter = ('status', 'project')
    search_fields = ('title', 'project__title')
