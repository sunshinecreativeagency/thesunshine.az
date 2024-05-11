from django.contrib import admin
from django.urls import path

from .views import CategoryListView, ProjectListView, ProjectView

urlpatterns = [
    path("categories/", CategoryListView.as_view()),
    path("list/", ProjectListView.as_view()),
    path("<slug>/", ProjectView.as_view()),
]
