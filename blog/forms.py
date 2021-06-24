from django import forms
from .widgets import CustomClearableFileInput
from .models import BlogPost
from .models import Comment


class BlogForm(forms.ModelForm):
    """
    Form to create blog
    """

    class Meta:
        model = BlogPost
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)


class CommentForm(forms.ModelForm):
    """
    Form to add comments to blog
    """

    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
