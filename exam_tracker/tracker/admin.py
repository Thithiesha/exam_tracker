from django.contrib import admin
from .models import Subject, ExamScore

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Columns to display in the list view
    search_fields = ('name',)  # Search functionality for the list view

@admin.register(ExamScore)
class ExamScoreAdmin(admin.ModelAdmin):
    list_display = ('subject', 'date', 'score')  # Columns to display in the list view
    list_filter = ('subject', 'date')  # Add filters in the sidebar
    search_fields = ('subject__name',)  # Search functionality for the list view

    # Optionally, customize the form used for adding/editing records
    # fields = ('subject', 'date', 'score')  # Define the fields in the form
    # exclude = ('field_to_exclude',)  # Exclude fields from the form
    # readonly_fields = ('date',)  # Make fields read-only

