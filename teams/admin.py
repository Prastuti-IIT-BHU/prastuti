from django.contrib import admin
from .models import Team
# from import_export.admin import ImportExportModelAdmin


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_name','team_event','team_active')