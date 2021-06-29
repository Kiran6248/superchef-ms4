from django.contrib import admin
from .models import BlogPost, Comment


class BlogPostAdmin(admin.ModelAdmin):
    """
    Admin display for blog post.
    """
    list_display = (
        'title',
        'author',
        'created_on',
        'status',
    )
    list_filter = ("status",)
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment, CommentAdmin)
