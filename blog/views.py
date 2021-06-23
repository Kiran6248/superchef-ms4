from django.shortcuts import render

from .models import BlogPost


def all_blog_posts(request):
    """
    A view to return all the blog posts
    """
    blogs = BlogPost.objects.all()
    context = {
        'blogs': blogs,
    }

    return render(request, 'blog/blog_posts.html', context)
