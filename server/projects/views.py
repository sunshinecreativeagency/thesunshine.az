from django.shortcuts import render
from rest_framework import generics, serializers

from .models import Category, Project, ProjectImage


# Create your views here.
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name", "slug")


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ["id", "image"]


class ProjectSerializer(serializers.ModelSerializer):
    images = ProjectImageSerializer(many=True)

    class Meta:
        model = Project
        fields = "__all__"


class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.filter(status="published")
    serializer_class = ProjectSerializer


class ProjectView(generics.RetrieveAPIView):
    queryset = Project.objects.filter(status="published")
    serializer_class = ProjectSerializer
    lookup_field = "slug"
