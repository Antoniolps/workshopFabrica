from rest_framework import serializers
from apps.post.models import Post
from apps.user.models import User
from apps.coment.models import Comment

class PostSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')

    class Meta:
        model = Post
        fields = ["id", "title", "content", "date_posted", "author"]
    