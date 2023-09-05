from rest_framework import serializers
from apps.user.models import User
from apps.post.models import Post


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        fields = ["id","name", "email"]