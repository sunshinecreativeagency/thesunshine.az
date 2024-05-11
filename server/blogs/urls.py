from django.contrib import admin
from django.urls import path

from .views import CategoryListView, BlogListView, BlogView

urlpatterns = [
    path("categories/", CategoryListView.as_view()),
    path("list/", BlogListView.as_view()),
    path("<slug>/", BlogView.as_view()),
]
