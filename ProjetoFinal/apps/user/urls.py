from django.urls import path,include
from rest_framework import routers
from apps.user.api.viewsets import UserViewSet

"""
API endpoint permite acessar e modificar o user
"""

router = routers.DefaultRouter()
router.register("", UserViewSet, basename="user")

urlpatterns = [
    path('', include(router.urls)),
]