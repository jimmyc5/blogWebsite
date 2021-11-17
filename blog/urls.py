from django.urls import path
from . import views

app_name='blog'
urlpatterns= [
    path('',views.blogPost, name='blogPost'),
    path('inputComment',views.inputComment,name='inputComment')
]