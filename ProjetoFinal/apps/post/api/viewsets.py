from rest_framework.viewsets import ModelViewSet

from apps.post.models import Post
from .serializers import PostSerializer

class PostViewSet(ModelViewSet):
    #Setando que quero todos os dados que estão na tabela post 
    queryset = Post.objects.all()

    serializer_class = PostSerializer