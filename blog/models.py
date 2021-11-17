from django.db import models

# Create your models here.

class BlogPost(models.Model):
    article_title = models.CharField(max_length=200)
    article_text = models.TextField(max_length=5000)
    article_author = models.CharField(max_length=100)

class Comment(models.Model):
    comment_author = models.CharField(max_length=100, default="anonymous")
    comment_text = models.CharField(max_length=1000)