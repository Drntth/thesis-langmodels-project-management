from django.contrib import admin
from .models import Project, ProjectStatus, ProjectRole, ProjectMember


@admin.register(ProjectStatus)
class ProjectStatusAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "status", "deadline", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("name", "owner__username")


@admin.register(ProjectRole)
class ProjectRoleAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(ProjectMember)
class ProjectMemberAdmin(admin.ModelAdmin):
    list_display = ("user", "project", "role")
    list_filter = ("role", "project")
    search_fields = ("user__username", "project__name")
