from django.urls import path

from .views import PostView, SinglePostView

app_name = 'blog'

urlpatterns = [
    path('posts/', PostView.as_view(), name='api_posts'),
    path('posts/<int:pk>/', SinglePostView.as_view(), name='api_by_post')
]