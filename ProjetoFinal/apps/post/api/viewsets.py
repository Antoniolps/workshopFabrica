from rest_framework.viewsets import ModelViewSet

from apps.post.models import Post
from .serializers import PostSerializer
from apps.user.models import User

from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

class PostViewSet(ModelViewSet):
    #Setando que quero todos os dados que estão na tabela post 
    queryset = Post.objects.all()

    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        requisicao = self.request.query_params.get("usuario")

        if requisicao:
            if User.objects.get(name = requisicao):
                return Post.objects.filter(author = User.objects.get(name = requisicao))
            else:
                return Response("User not found")
            
        return Post.objects.all()
    