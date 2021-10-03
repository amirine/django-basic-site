from django.urls import path

from .views import PostView

app_name = 'blog'

urlpatterns = [
    path('posts/', PostView.as_view(), name='api_posts'),
    path('posts/<int:pk>/', PostView.as_view(), name='api_by_post')
]