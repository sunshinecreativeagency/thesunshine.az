from django.contrib import admin
from .models import Project, ProjectImage, Category
from django.db import models


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "timestamp",
        "status",
        "category",
    ]
    list_filter = ["status", "category"]
    search_fields = ["title"]
    inlines = [ProjectImageInline]


admin.site.register(Category)
