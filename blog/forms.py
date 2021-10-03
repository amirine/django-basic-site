from django.forms import ModelForm
from .models import Post, Category


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'category')


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('name',)