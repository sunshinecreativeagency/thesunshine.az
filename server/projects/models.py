from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[("draft", "Draft"), ("published", "Published")],
        default="draft",
    )
    image = models.ImageField(upload_to="project_covers/", null=True, blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="project_images/", null=True, blank=True)
