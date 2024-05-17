"""smnglofnet URL Configuration"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # ------------------------------------------------
    # ADMIN
    path('admin/', admin.site.urls),

    # ------------------------------------------------
    # DJOSER
    path('api/v1/auth/', include('djoser.urls')),
    # path('api/v1/auth/', include('djoser.urls.jwt')),
    path('api/v1/auth/', include('djoser.urls.authtoken')),

    # ------------------------------------------------
    # APP AUTHS URL
    path('', include('auths.urls')),

    # ------------------------------------------------
    # USER FOLLOWS
    path('', include('friends.urls')),

    # ------------------------------------------------
    # MESSAGES
    path('', include('chats.urls')),

    # ------------------------------------------------
    # MESSAGES IN GROUPS
    path('', include('chat_groups.urls')),

    # ------------------------------------------------
    # DROP POST IN PERSONAL ACCOUNT
    path('', include('posts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
