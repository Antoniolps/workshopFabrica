from rest_framework import serializers
from apps.coment.models import Comment
from apps.post.models import Post
from apps.user.models import User

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')
    post = serializers.SlugRelatedField(queryset=Post.objects.all(), slug_field='title')

    class Meta:
        model = Comment
        fields = ['text', 'post','author']