from django.contrib import admin
from .models import Blog, Category
from tinymce.widgets import TinyMCE
from django.db import models


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {"widget": TinyMCE()},
    }
    list_display = [
        "title",
        "timestamp",
        "status",
        "category",
    ]
    list_filter = ["status", "category"]
    search_fields = ["title", "body"]


admin.site.register(Category)
