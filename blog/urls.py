from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, home_page_view, posts_page_view, by_category_view
from .views import PostFormView, CategoryFormView

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='user')

urlpatterns = [
    path('home/', home_page_view, name='home'),
    path('posts/', posts_page_view, name='posts'),
    path('posts/<int:category_id>/', by_category_view, name='by_category'),
    path('new_post/', PostFormView.as_view(), name='new_post'),
    path('new_category/', CategoryFormView.as_view(), name='new_category'),
    path('api/', include((router.urls, 'blog'))),
]
