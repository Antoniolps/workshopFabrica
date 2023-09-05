from rest_framework.viewsets import ModelViewSet

from apps.coment.models import Comment
from .serializers import CommentSerializer

from rest_framework.pagination import LimitOffsetPagination

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = LimitOffsetPagination