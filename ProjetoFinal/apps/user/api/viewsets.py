from rest_framework.viewsets import ModelViewSet
from apps.user.models import User
from .serializers import UserSerializer

from rest_framework.pagination import LimitOffsetPagination

class UserViewSet(ModelViewSet):
    #quero todos os dados da tabela task 
    queryset = User.objects.all()
    serializer_class = UserSerializer

    pagination_class = LimitOffsetPagination