from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('post/', include('apps.post.urls')),

    path('user/', include('apps.user.urls')),

    path('', include('apps.index.urls'))
]
