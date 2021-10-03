from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from rest_framework import viewsets

from .models import Post, Category
from .serializers import PostSerializer
from .forms import PostForm, CategoryForm


class PostViewSet(viewsets.ModelViewSet):
    """View for Post model serialization"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer


def home_page_view(request):
    """View for Home page"""
    context = {
        'categories': Category.objects.all()
    }
    return render(request, 'blog/home_page.html', context)


def posts_page_view(request):
    """View for Posts page: list of posts with description"""
    context = {
        'posts': Post.objects.all(),
        'categories': Category.objects.all()
    }
    return render(request, 'blog/posts_page.html', context)


def by_category_view(request, category_id):
    """View for Category page: list of posts with description related to {category_id} category"""
    posts = Post.objects.filter(category=category_id)
    current_category = Category.objects.get(pk=category_id)
    categories = Category.objects.all()
    context = {
        'posts': posts,
        'current_category': current_category,
        'categories': categories,
    }
    return render(request, 'blog/by_category_page.html', context)


class PostFormView(CreateView):
    """View for adding new posts information:
            form with {title, text, category} fields for Post model"""
    template_name = 'blog/add_new_post_page.html'
    form_class = PostForm
    success_url = reverse_lazy('posts')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class CategoryFormView(CreateView):
    """View for adding new categories information:
                form with {name} field for Category model"""
    template_name = 'blog/add_new_category_page.html'
    form_class = CategoryForm
    success_url = reverse_lazy('new_post')
