from django.contrib import admin

from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'salary')
    search_fields = ('title', 'company', 'location', 'salary')
    list_filter = ('location', )
    # ordering = ('title', 'company', 'location', 'salary')

