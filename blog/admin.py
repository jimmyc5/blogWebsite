from django.contrib import admin
from .models import Comment, BlogPost

admin.site.register(BlogPost)
admin.site.register(Comment)
