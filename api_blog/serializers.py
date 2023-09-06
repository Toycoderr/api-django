from rest_framework import serializers
from blog.models import BlogPost, Category, Tag

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')

class BlogPostSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = BlogPost
        fields = ('id', 'title', 'slug', 'published_date', 'updated_date', 
                  'intro', 'content', 'categories', 'tags', 'is_published', 'is_featured', 'cover_image')
