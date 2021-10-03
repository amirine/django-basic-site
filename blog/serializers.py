from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    date = serializers.DateTimeField()
    text = serializers.CharField(max_length=200)
    category_id = serializers.IntegerField()

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.date = validated_data.get('date', instance.date)
        instance.text = validated_data.get('text', instance.text)
        instance.category_id = validated_data.get('category_id', instance.category_id)
        instance.save()
        return instance
