from django.shortcuts import render
from rest_framework import generics, serializers

from .models import Category, Blog


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name", "slug")


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"


class BlogListView(generics.ListAPIView):
    queryset = Blog.objects.filter(status="published")
    serializer_class = BlogSerializer


class BlogView(generics.RetrieveAPIView):
    queryset = Blog.objects.filter(status="published")
    serializer_class = BlogSerializer
    lookup_field = "slug"
