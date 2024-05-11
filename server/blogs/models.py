from django.db import models
from tinymce import models as tinymce_models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = tinymce_models.HTMLField()
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[("draft", "Draft"), ("published", "Published")],
        default="draft",
    )
    image = models.ImageField(upload_to="blog_covers/", null=True, blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
