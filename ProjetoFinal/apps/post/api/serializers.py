from rest_framework import serializers
from apps.post.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post

        fields = ["id", "title", "content", "date_posted", "author"]
    