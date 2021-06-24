from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import BlogPost
from .forms import BlogForm


def all_blog_posts(request):
    """
    A view to return all the blog posts
    """
    blogs = BlogPost.objects.all()
    context = {
        'blogs': blogs,
    }

    return render(request, 'blog/blog_posts.html', context)


def blog_detail(request, slug):
    """
    A view to return individual blog posts
    """
    blog = get_object_or_404(BlogPost, slug=slug)
    context = {
        'blog': blog,
    }

    return render(request, 'blog/blog_detail.html', context)


@login_required
def add_blog(request):
    """
    Add a blog to the blog page
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, this is onlt for store qwners.')
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            new_blog = form.save()
            messages.success(request, 'Successfully added blog.')
            return redirect(reverse('blog_detail', args=[new_blog.slug]))
        else:
            messages.error(
                request, 'Failed to add blog. \
                    Please check the form is valid and try again.')
    else:
        form = BlogForm()
    
    template = 'blog/add_blog.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
