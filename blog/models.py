from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    # Metadata
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300, unique_for_date='published_date')
    published_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)

    # Content
    intro = models.TextField()
    content = models.TextField()

    # Categories and Tags
    categories = models.ManyToManyField(Category, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    # Publishing options
    is_published = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)

    # Image
    cover_image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title