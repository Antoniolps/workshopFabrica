from django.urls import path, include
from rest_framework import routers

from apps.coment.api.viewsets import CommentViewSet

router = routers.DefaultRouter()

router.register('', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls))
]
