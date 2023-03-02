from django.forms import ModelForm

from .models import Post, Comment

class BlogForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['author','slug']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ['post']
