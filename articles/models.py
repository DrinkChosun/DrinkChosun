from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.CharField(max_length=20, default='anonymous')

class Comment(models.Model):
    content = models.CharField(max_length=200)
    user = models.CharField(max_length=20, default='anonymous')
    article = models.ForeignKey(Article, on_delete=models.CASCADE)