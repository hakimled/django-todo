from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'is_Completed', 'created_at', 'updated_at')  # Fields shown in the list view
    list_filter = ('is_Completed', 'created_at')  # Add filtering options
    search_fields = ('task',)  # Enable search by task name
    ordering = ('-created_at',)  # Order by newest first
    list_editable = ('is_Completed',)  # Allow inline editing for completion status
    date_hierarchy = 'created_at'  # Adds a navigation by date
