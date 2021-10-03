from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post
from .serializers import PostSerializer


class PostView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response({"posts": serializer.data})

    def post(self, request):
        new_post = request.data.get('post')
        serializer = PostSerializer(data=new_post)
        if serializer.is_valid(raise_exception=True):
            new_post_saved = serializer.save()
        return Response({
            "success": f"Post {new_post_saved.title} created successfully."
        })

    def put(self, request, pk):
        saved_post = get_object_or_404(Post.objects.all(), pk=pk)
        data = request.data.get('post')
        serializer = PostSerializer(instance=saved_post, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            post_saved = serializer.save()
        return Response({
            "success": f"Post {post_saved.title} updated successfully."
        })

    def delete(self, request, pk):
        post_to_delete = get_object_or_404(Post, pk=pk)
        post_to_delete.delete()
        return Response({
            "success": f"Post with id {pk} successfully deleted."
        }, status=204)
