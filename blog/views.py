from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import BlogPost, Comment
from django.urls import reverse

def blogPost(request):
    blog = BlogPost.objects.all()[0]
    comments = Comment.objects.all()
    return render(request, 'blog/blogPost.html', {"blog_post":blog, "comments":comments})
# Create your views here.

def inputComment(request):
    if(request.POST.get('commentText')==False or request.POST.get('commentText').strip()==""):
        return HttpResponseRedirect(reverse('blog:blogPost', args=()))
    else:
        if(request.POST.get('commentAuthor','anonymous')==""):
            newComment = Comment(comment_author='anonymous',comment_text=request.POST["commentText"])
        else:
            newComment = Comment(comment_author=request.POST.get('commentAuthor','anonymous'),comment_text=request.POST["commentText"])
        newComment.save()
        return HttpResponseRedirect(reverse('blog:blogPost', args=()))

        