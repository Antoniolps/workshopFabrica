from django.urls import path, include
from rest_framework import routers
from apps.post.api.viewsets import PostViewSet

#Criando o endpoint
router = routers.DefaultRouter()

router.register("", PostViewSet, basename="post")

urlpatterns = [
    path("", include(router.urls))
]