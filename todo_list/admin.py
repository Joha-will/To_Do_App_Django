from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):

    list_display = ('task', 'is_completed', 'updated_on',)
    search_fields = ('task', 'is_completed',)


admin.site.register(Task, TaskAdmin,)
